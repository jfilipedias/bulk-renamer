from __future__ import annotations
from pathlib import Path
from os import path
from random import randint

from rich import box
from rich.console import Console
from rich.table import Table
from typer import confirm, echo, prompt


console = Console()


def get_cwd_file_paths() -> list[Path]:
    """Return a list of all file paths from the current working directory."""

    cwd = Path.cwd()
    glob = cwd.glob("*")
    files = filter(lambda x: x.is_file(), glob)

    return files


def get_value_input(
    new_value_message: str, old_value_message: str = ""
) -> tuple(str, str):
    """Get the args values from the user input."""

    old_value = prompt(old_value_message) if old_value_message else None
    new_value = prompt(new_value_message) if new_value_message else None

    return (new_value, old_value)


def rename_files(old_filenames: list[str], new_filenames: list[str]) -> None:
    """Rename a list of files from current working directory."""

    if len(old_filenames) != len(new_filenames):
        return

    with console.status("Renaming files"):
        for i in range(len(old_filenames)):
            extension = path.splitext(old_filenames[i])[1]
            temp_name = f"tempfile_{randint(1000, 9999)}{extension}"

            file_path = Path(old_filenames[i])
            file_path = file_path.rename(Path(temp_name))
            file_path.rename(Path(new_filenames[i]))

    console.print("All files have been renamed.")


def show_changes(old_filenames: list[str], new_filenames: list[str]) -> None:
    """Show a table with the filenames diffs"""

    table = Table()
    table.box = box.SIMPLE_HEAD

    table.add_column("Current Filenames", header_style="bold cyan", style="cyan")
    table.add_column("")
    table.add_column("New Filenames", header_style="bold green", style="green")

    arrows = [name.replace(name, "->") for name in old_filenames]
    table.add_row("\n".join(old_filenames), "\n".join(arrows), "\n".join(new_filenames))

    console.print(table)


def confirm_changes(old_filenames: list[str], new_filenames: list[str]) -> None:
    """Show the changes and ask the user to confirm the changes."""

    show_changes(old_filenames, new_filenames)

    if confirm("Are you sure you want to rename these files?", default=True):
        rename_files(old_filenames, new_filenames)
    else:
        echo("Don't worry, no changes have been made.")
