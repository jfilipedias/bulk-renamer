from pathlib import Path

import typer

from .utils import functions

app = typer.Typer()


@app.command()
def remove() -> None:
    print("Calling remove command...")


@app.command()
def rename() -> None:
    print("Calling rename command...")


@app.command()
def replace(
    old_value: str = typer.Argument(..., help="The string to shearch for"),
    new_value: str = typer.Argument(
        ..., help="The string to replace the old value with"
    ),
) -> None:
    """
    Replaces a specified string in the file name with another specified string.
    """

    files_path = functions.get_all_files_in_cwd()

    for file in files_path:
        file_name = file.stem

        if not file_name:
            continue

        extension = file.suffix

        file_name = file_name.replace(old_value, new_value)
        file_name = f"{file_name}{extension}"

        file.rename(Path(file.parent, file_name))
