from pathlib import Path

import typer

from .utils import functions

app = typer.Typer()


@app.command()
def prefix(
    value: str = typer.Argument(
        ..., help="The string to be added to the beginning of the filename."
    )
) -> None:
    "Adds a string to the beginning of the filename."

    add_string_to_filename(value, is_suffix=False)


@app.command()
def suffix(
    value: str = typer.Argument(
        ..., help="The string to be added to the ending of the filename."
    )
) -> None:
    "Adds a string to the ending of the filename."

    add_string_to_filename(value)


def add_string_to_filename(value: str, is_suffix: bool = True) -> None:
    """Adds a prefix or a suffix to a filename."""

    files_path = functions.get_all_files_in_cwd()

    for file in files_path:
        filename = file.stem

        if not filename:
            continue

        extension = file.suffix

        filename = f"{filename}{value}" if is_suffix else f"{value}{filename}"
        filename = f"{filename}{extension}"

        file.rename(Path(file.parent, filename))
