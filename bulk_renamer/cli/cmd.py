import typer

from bulk_renamer.utils.functions import get_cwd_file_paths, confirm_changes

app = typer.Typer()


@app.command()
def remove(
    value: str = typer.Argument(..., help="The string to remove from filename.")
) -> None:
    """Remove a specified string from the filename."""

    current_file_paths = get_cwd_file_paths()
    current_filenames = []
    new_filenames = []

    for path in current_file_paths:
        name = path.stem
        extension = path.suffix

        if not name:
            continue

        new_name = name.replace(value, "")
        new_filenames.append(f"{new_name}{extension}")
        current_filenames.append(f"{name}{extension}")

    confirm_changes(current_filenames, new_filenames)


@app.command()
def replace(
    old_value: str = typer.Argument(..., help="The string to shearch for."),
    new_value: str = typer.Argument(
        ..., help="The string to replace the old value with."
    ),
) -> None:
    """Replaces a specified string in the filename with another specified string."""

    current_file_paths = get_cwd_file_paths()
    current_filenames = []
    new_filenames = []

    for path in current_file_paths:
        name = path.stem
        extension = path.suffix

        if not name:
            continue

        new_name = name.replace(old_value, new_value)
        new_filenames.append(f"{new_name}{extension}")
        current_filenames.append(f"{name}{extension}")

    confirm_changes(current_filenames, new_filenames)
