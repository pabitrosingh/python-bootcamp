import tempfile
import unittest
from pathlib import Path

from fastapi.testclient import TestClient

from Month_4.Week_4.Project.crm import create_app


class CrmApiTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        database_path = Path(self.temporary_directory.name) / "crm.db"
        self.client = TestClient(create_app(f"sqlite:///{database_path}"))
        self.client.__enter__()

    def tearDown(self) -> None:
        self.client.__exit__(None, None, None)
        self.temporary_directory.cleanup()

    def test_customer_crud_and_note_relationship(self):
        created = self.client.post(
            "/customers",
            json={
                "name": "  Ada Lovelace ",
                "email": " ADA@example.com ",
                "company": "Analytical Engines",
            },
        )
        self.assertEqual(created.status_code, 201)
        self.assertEqual(created.json()["name"], "Ada Lovelace")
        self.assertEqual(created.json()["email"], "ada@example.com")
        self.assertTrue(created.json()["created_at"].endswith("Z"))
        customer_id = created.json()["id"]

        note = self.client.post(
            f"/customers/{customer_id}/notes", json={"body": "Follow up next week"}
        )
        self.assertEqual(note.status_code, 201)
        self.assertEqual(note.json()["customer_id"], customer_id)
        self.assertTrue(note.json()["created_at"].endswith("Z"))
        self.assertEqual(len(self.client.get(f"/customers/{customer_id}/notes").json()), 1)

        updated = self.client.patch(
            f"/customers/{customer_id}", json={"company": None}
        )
        self.assertEqual(updated.status_code, 200)
        self.assertIsNone(updated.json()["company"])
        self.assertEqual(len(self.client.get("/customers").json()), 1)

        deleted = self.client.delete(f"/customers/{customer_id}")
        self.assertEqual(deleted.status_code, 204)
        self.assertEqual(self.client.get(f"/customers/{customer_id}").status_code, 404)

    def test_duplicate_email_is_a_conflict(self):
        self.client.post(
            "/customers", json={"name": "First", "email": "person@example.com"}
        )
        duplicate = self.client.post(
            "/customers", json={"name": "Second", "email": "PERSON@example.com"}
        )
        self.assertEqual(duplicate.status_code, 409)

    def test_missing_customer_and_empty_patch_are_rejected(self):
        self.assertEqual(self.client.get("/customers/88").status_code, 404)
        self.assertEqual(
            self.client.post("/customers/88/notes", json={"body": "Note"}).status_code,
            404,
        )
        self.client.post(
            "/customers", json={"name": "Grace", "email": "grace@example.com"}
        )
        self.assertEqual(self.client.patch("/customers/1", json={}).status_code, 422)


if __name__ == "__main__":
    unittest.main()
