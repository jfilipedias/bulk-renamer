from __future__ import annotations
from pathlib import Path


def get_all_files_in_cwd() -> list[Path]:
    cwd_path = Path.cwd()
    glob = cwd_path.glob("*")
    files = [item for item in glob if item.is_file()]

    return files
