from __future__ import annotations
from pathlib import Path
from os import path
from random import randint


def get_cwd_file_paths() -> list[Path]:
    """Return a list of all file paths from the current working directory."""

    cwd_path = Path.cwd()
    glob = cwd_path.glob("*")
    files = filter(lambda x: x.is_file(), glob)

    return files


def rename_file(file_path: Path, new_filename: str) -> None:
    """Rename a file of a give path."""

    extension = path.splitext(new_filename)[1]
    temp_name = f"tempfile_{randint(1000, 9999)}{extension}"

    file_path = file_path.rename(Path(file_path.parent, temp_name))
    file_path.rename(Path(file_path.parent, new_filename))
