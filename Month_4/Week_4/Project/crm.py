"""A customer and notes API using SQLAlchemy 2.x."""

from __future__ import annotations

from contextlib import asynccontextmanager
from collections.abc import AsyncIterator, Iterator
from datetime import datetime, timezone
import os
from pathlib import Path

from fastapi import Depends, FastAPI, HTTPException, Response, status
from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator
from sqlalchemy import DateTime, ForeignKey, String, create_engine, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship, sessionmaker


class Base(DeclarativeBase):
    pass


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(320), unique=True, index=True)
    company: Mapped[str | None] = mapped_column(String(160), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    notes: Mapped[list[CustomerNote]] = relationship(
        back_populates="customer", cascade="all, delete-orphan"
    )


class CustomerNote(Base):
    __tablename__ = "customer_notes"

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"), nullable=False)
    body: Mapped[str] = mapped_column(String(4_000), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    customer: Mapped[Customer] = relationship(back_populates="notes")


def _normalize_email(value: str | None) -> str | None:
    if value is None:
        return None
    email = value.strip().lower()
    if (
        email.count("@") != 1
        or any(character.isspace() for character in email)
        or "." not in email.rsplit("@", maxsplit=1)[1]
    ):
        raise ValueError("email must be a valid address")
    return email


def _as_utc(value: datetime) -> datetime:
    if value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc)


class CustomerCreate(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    email: str = Field(min_length=3, max_length=320)
    company: str | None = Field(default=None, max_length=160)

    @field_validator("name")
    @classmethod
    def strip_name(cls, value: str) -> str:
        name = value.strip()
        if not name:
            raise ValueError("name must not be blank")
        return name

    @field_validator("email")
    @classmethod
    def normalize_email(cls, value: str) -> str:
        email = _normalize_email(value)
        if email is None:
            raise ValueError("email is required")
        return email

    @field_validator("company")
    @classmethod
    def strip_company(cls, value: str | None) -> str | None:
        return value.strip() if value is not None else None


class CustomerUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=120)
    email: str | None = Field(default=None, min_length=3, max_length=320)
    company: str | None = Field(default=None, max_length=160)

    @field_validator("name")
    @classmethod
    def strip_name(cls, value: str | None) -> str | None:
        if value is None:
            return None
        name = value.strip()
        if not name:
            raise ValueError("name must not be blank")
        return name

    @field_validator("email")
    @classmethod
    def normalize_email(cls, value: str | None) -> str | None:
        return _normalize_email(value)

    @field_validator("company")
    @classmethod
    def strip_company(cls, value: str | None) -> str | None:
        return value.strip() if value is not None else None

    @model_validator(mode="after")
    def validate_patch(self) -> CustomerUpdate:
        if not self.model_fields_set:
            raise ValueError("at least one field must be supplied")
        if any(
            getattr(self, field) is None
            for field in self.model_fields_set
            if field != "company"
        ):
            raise ValueError("name and email cannot be null")
        return self


class CustomerRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: str
    company: str | None
    created_at: datetime

    @field_validator("created_at")
    @classmethod
    def make_created_at_utc(cls, value: datetime) -> datetime:
        return _as_utc(value)


class NoteCreate(BaseModel):
    body: str = Field(min_length=1, max_length=4_000)

    @field_validator("body")
    @classmethod
    def strip_body(cls, value: str) -> str:
        body = value.strip()
        if not body:
            raise ValueError("note body must not be blank")
        return body


class NoteRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    customer_id: int
    body: str
    created_at: datetime

    @field_validator("created_at")
    @classmethod
    def make_created_at_utc(cls, value: datetime) -> datetime:
        return _as_utc(value)


def create_app(database_url: str | None = None) -> FastAPI:
    default_database = Path(__file__).with_name("crm.db").resolve()
    url = (
        database_url
        or os.environ.get("CRM_DATABASE_URL")
        or f"sqlite:///{default_database}"
    )
    engine_options = {"connect_args": {"check_same_thread": False}} if url.startswith(
        "sqlite"
    ) else {}
    engine = create_engine(url, **engine_options)
    session_factory = sessionmaker(bind=engine, expire_on_commit=False)

    @asynccontextmanager
    async def lifespan(_: FastAPI) -> AsyncIterator[None]:
        Base.metadata.create_all(engine)
        yield
        engine.dispose()

    app = FastAPI(title="CRM Backend", version="1.0.0", lifespan=lifespan)

    def get_session() -> Iterator[Session]:
        with session_factory() as session:
            yield session

    def commit_or_conflict(session: Session) -> None:
        try:
            session.commit()
        except IntegrityError as error:
            session.rollback()
            raise HTTPException(
                status_code=409, detail="A customer with that email already exists"
            ) from error

    @app.post(
        "/customers",
        response_model=CustomerRead,
        status_code=status.HTTP_201_CREATED,
    )
    def create_customer(
        payload: CustomerCreate, session: Session = Depends(get_session)
    ) -> Customer:
        customer = Customer(**payload.model_dump())
        session.add(customer)
        commit_or_conflict(session)
        session.refresh(customer)
        return customer

    @app.get("/customers", response_model=list[CustomerRead])
    def list_customers(session: Session = Depends(get_session)) -> list[Customer]:
        statement = select(Customer).order_by(Customer.id)
        return list(session.scalars(statement).all())

    @app.get("/customers/{customer_id}", response_model=CustomerRead)
    def get_customer(
        customer_id: int, session: Session = Depends(get_session)
    ) -> Customer:
        customer = session.get(Customer, customer_id)
        if customer is None:
            raise HTTPException(status_code=404, detail="Customer not found")
        return customer

    @app.patch("/customers/{customer_id}", response_model=CustomerRead)
    def update_customer(
        customer_id: int,
        payload: CustomerUpdate,
        session: Session = Depends(get_session),
    ) -> Customer:
        customer = session.get(Customer, customer_id)
        if customer is None:
            raise HTTPException(status_code=404, detail="Customer not found")
        for field, value in payload.model_dump(exclude_unset=True).items():
            setattr(customer, field, value)
        commit_or_conflict(session)
        session.refresh(customer)
        return customer

    @app.delete(
        "/customers/{customer_id}", status_code=status.HTTP_204_NO_CONTENT
    )
    def delete_customer(
        customer_id: int, session: Session = Depends(get_session)
    ) -> Response:
        customer = session.get(Customer, customer_id)
        if customer is None:
            raise HTTPException(status_code=404, detail="Customer not found")
        session.delete(customer)
        session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    @app.post(
        "/customers/{customer_id}/notes",
        response_model=NoteRead,
        status_code=status.HTTP_201_CREATED,
    )
    def add_note(
        customer_id: int,
        payload: NoteCreate,
        session: Session = Depends(get_session),
    ) -> CustomerNote:
        customer = session.get(Customer, customer_id)
        if customer is None:
            raise HTTPException(status_code=404, detail="Customer not found")
        note = CustomerNote(customer=customer, body=payload.body)
        session.add(note)
        session.commit()
        session.refresh(note)
        return note

    @app.get("/customers/{customer_id}/notes", response_model=list[NoteRead])
    def list_notes(
        customer_id: int, session: Session = Depends(get_session)
    ) -> list[CustomerNote]:
        customer = session.get(Customer, customer_id)
        if customer is None:
            raise HTTPException(status_code=404, detail="Customer not found")
        statement = (
            select(CustomerNote)
            .where(CustomerNote.customer_id == customer_id)
            .order_by(CustomerNote.id)
        )
        return list(session.scalars(statement).all())

    return app


app = create_app()
