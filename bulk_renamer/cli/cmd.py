import typer

from ..utils.functions import get_cwd_file_paths, rename_file

app = typer.Typer()


@app.command()
def remove(
    value: str = typer.Argument(..., help="The string to remove from filename.")
) -> None:
    """Remove a specified string from the filename."""

    paths = get_cwd_file_paths()

    for path in paths:
        name = paths.stem
        extension = path.suffix

        if not name:
            continue

        name = name.replace(value, "")
        filename = f"{name}{extension}"

        rename_file(path, filename)


@app.command()
def replace(
    old_value: str = typer.Argument(..., help="The string to shearch for."),
    new_value: str = typer.Argument(
        ..., help="The string to replace the old value with."
    ),
) -> None:
    """Replaces a specified string in the filename with another specified string."""

    paths = get_cwd_file_paths()

    for path in paths:
        name = path.stem

        if not name:
            continue

        extension = path.suffix
        name = name.replace(old_value, new_value)
        filename = f"{name}{extension}"

        rename_file(path, filename)
