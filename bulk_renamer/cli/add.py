import typer

from ..utils.functions import get_cwd_file_paths, rename_file

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

    paths = get_cwd_file_paths()

    for path in paths:
        name = path.stem
        extension = path.suffix

        if not name:
            continue

        name = f"{name}{value}" if is_suffix else f"{value}{name}"
        filename = f"{name}{extension}"

        rename_file(path, filename)
