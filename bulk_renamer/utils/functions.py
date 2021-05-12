from __future__ import annotations
from pathlib import Path


def get_cwd_file_paths() -> list[Path]:
    """Return a list of all file paths from the current working directory."""

    cwd_path = Path.cwd()
    glob = cwd_path.glob("*")
    files = filter(lambda x: x.is_file(), glob)

    return files


def rename_file(file_path: Path, new_filename: str) -> None:
    """Rename a file of a give path."""

    file_path.rename(Path(file_path.parent, new_filename))
