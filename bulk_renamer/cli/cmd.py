from pathlib import Path

import typer

from .utils import functions

app = typer.Typer()


@app.command()
def remove(
    value: str = typer.Argument(..., help="The string to remove from filename.")
) -> None:
    """Remove a specified string from the filename."""

    files_path = functions.get_all_files_in_cwd()

    for file in files_path:
        filename = file.stem

        if not filename:
            continue

        extension = file.suffix

        filename = filename.replace(value, "")
        filename = f"{filename}{extension}"

        file.rename(Path(file.parent, filename))


@app.command()
def replace(
    old_value: str = typer.Argument(..., help="The string to shearch for."),
    new_value: str = typer.Argument(
        ..., help="The string to replace the old value with."
    ),
) -> None:
    """Replaces a specified string in the filename with another specified string."""

    files_path = functions.get_all_files_in_cwd()

    for file in files_path:
        filename = file.stem

        if not filename:
            continue

        extension = file.suffix

        filename = filename.replace(old_value, new_value)
        filename = f"{filename}{extension}"

        file.rename(Path(file.parent, filename))
