"""Preview or apply extension-based file organization."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import logging
from pathlib import Path


logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Move:
    """A proposed source and destination path."""

    source: Path
    destination: Path


def _available_destination(directory: Path, filename: str) -> Path:
    candidate = directory / filename
    if not candidate.exists():
        return candidate

    path = Path(filename)
    suffix = path.suffix
    stem = path.name[: -len(suffix)] if suffix else path.name
    index = 1
    while True:
        candidate = directory / f"{stem}_{index}{suffix}"
        if not candidate.exists():
            return candidate
        index += 1


def plan_organization(root: str | Path) -> tuple[Move, ...]:
    """Return planned moves for regular, non-symlink files directly under root."""
    directory = Path(root)
    if not directory.exists():
        raise FileNotFoundError(directory)
    if not directory.is_dir():
        raise NotADirectoryError(directory)

    planned_destinations: set[Path] = set()
    moves: list[Move] = []
    for source in sorted(directory.iterdir()):
        if source.is_symlink() or not source.is_file():
            continue
        extension = source.suffix.lower().lstrip(".") or "no_extension"
        destination_directory = directory / extension
        destination = _available_destination(destination_directory, source.name)
        while destination in planned_destinations:
            destination = _available_destination(
                destination_directory, destination.name
            )
        planned_destinations.add(destination)
        moves.append(Move(source, destination))
    return tuple(moves)


def apply_moves(moves: tuple[Move, ...]) -> tuple[Move, ...]:
    """Move planned files, raising on filesystem errors or destination conflicts."""
    completed: list[Move] = []
    for move in moves:
        if move.destination.exists():
            raise FileExistsError(move.destination)
        move.destination.parent.mkdir(parents=True, exist_ok=True)
        move.source.rename(move.destination)
        completed.append(move)
        logger.info("Moved %s to %s", move.source, move.destination)
    return tuple(completed)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, help="directory whose direct files to organize")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="perform moves; without this flag, only show the plan",
    )
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.WARNING,
        format="%(levelname)s: %(message)s",
    )

    try:
        moves = plan_organization(args.directory)
        for move in moves:
            print(f"{move.source} -> {move.destination}")
        if args.apply:
            completed = apply_moves(moves)
            print(f"Moved {len(completed)} file(s).")
        else:
            print(f"Preview only: {len(moves)} move(s). Use --apply to move files.")
    except OSError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
