import typer

from ..utils.functions import get_cwd_file_paths, confirm_changes

__doc__ = """Adds a string in the name case based on the subcommands."""

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

    current_file_paths = get_cwd_file_paths()
    current_filenames = []
    new_filenames = []

    for path in current_file_paths:
        name = path.stem
        extension = path.suffix

        if not name:
            continue

        new_name = f"{name}{value}" if is_suffix else f"{value}{name}"
        new_filenames.append(f"{new_name}{extension}")
        current_filenames.append(f"{name}{extension}")

    confirm_changes(current_filenames, new_filenames)
