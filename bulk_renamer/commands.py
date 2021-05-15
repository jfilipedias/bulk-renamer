import typer

from bulk_renamer.functions import get_cwd_file_paths, confirm_changes

app = typer.Typer()


@app.command()
def alternate() -> None:
    """Alternate the name characters between upper and lowercase."""

    current_file_paths = get_cwd_file_paths()
    current_filenames = []
    new_filenames = []

    for path in current_file_paths:
        name = path.stem
        extension = path.suffix

        if not name:
            continue

        formated_name = ""
        upper = True

        for char in name:
            formated_name += char.upper() if upper else char.lower()
            upper = not upper

        new_filenames.append(f"{formated_name}{extension}")
        current_filenames.append(f"{name}{extension}")

    confirm_changes(current_filenames, new_filenames)


@app.command()
def camel(
    whitespace: bool = typer.Option(
        False, "--whitespace", "-w", help="Maintains the filename whitespaces."
    )
) -> None:
    """Format the filename to camel case convention."""

    current_file_paths = get_cwd_file_paths()
    current_filenames = []
    new_filenames = []

    for path in current_file_paths:
        name = path.stem
        extension = path.suffix

        if not name:
            continue

        new_name = name.lower()
        new_name = new_name.title()
        new_name = new_name[:1].lower() + new_name[1:]

        if not whitespace:
            new_name = new_name.replace(" ", "")

        new_filenames.append(f"{new_name}{extension}")
        current_filenames.append(f"{name}{extension}")

    confirm_changes(current_filenames, new_filenames)


@app.command()
def lower() -> None:
    """Set the filename to lowercase."""

    current_file_paths = get_cwd_file_paths()
    current_filenames = []
    new_filenames = []

    for path in current_file_paths:
        name = path.stem
        extension = path.suffix

        if not name:
            continue

        new_name = name.lower()
        new_filenames.append(f"{new_name}{extension}")
        current_filenames.append(f"{name}{extension}")

    confirm_changes(current_filenames, new_filenames)


@app.command()
def kebab(
    upper: bool = typer.Option(
        False, "--upper", "-u", help="Set all characters to uppercase."
    )
) -> None:
    """Format the filename to kebab case convention."""

    current_file_paths = get_cwd_file_paths()
    current_filenames = []
    new_filenames = []

    for path in current_file_paths:
        name = path.stem
        extension = path.suffix

        if not name:
            continue

        new_name = name.upper() if upper else name.lower()
        new_name = new_name.replace(" ", "-")
        new_name = new_name.replace("_", "-")
        new_filenames.append(f"{new_name}{extension}")
        current_filenames.append(f"{name}{extension}")

    confirm_changes(current_filenames, new_filenames)


@app.command()
def pascal(
    whitespace: bool = typer.Option(
        False, "--whitespace", "-w", help="Maintains the filename whitespaces."
    )
) -> None:
    """Format the filename to pascal case convention."""

    current_file_paths = get_cwd_file_paths()
    current_filenames = []
    new_filenames = []

    for path in current_file_paths:
        name = path.stem
        extension = path.suffix

        if not name:
            continue

        new_name = name.title()

        if not whitespace:
            new_name = new_name.replace(" ", "")

        new_filenames.append(f"{new_name}{extension}")
        current_filenames.append(f"{name}{extension}")

    confirm_changes(current_filenames, new_filenames)


@app.command()
def prefix(
    value: str = typer.Argument(
        ..., help="The string to be added to the beginning of the filename."
    )
) -> None:
    "Adds a string to the beginning of the filename."

    add_string_to_filename(value, is_suffix=False)


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


@app.command()
def snake(
    upper: bool = typer.Option(
        False, "--upper", "-u", help="Set all characters to uppercase."
    )
) -> None:
    """Format the filename to snake case convention."""

    current_file_paths = get_cwd_file_paths()
    current_filenames = []
    new_filenames = []

    for path in current_file_paths:
        name = path.stem
        extension = path.suffix

        if not name:
            continue

        new_name = name.upper() if upper else name.lower()
        new_name = new_name.replace(" ", "_")
        new_name = new_name.replace("-", "_")
        new_filenames.append(f"{new_name}{extension}")
        current_filenames.append(f"{name}{extension}")

    confirm_changes(current_filenames, new_filenames)


@app.command()
def suffix(
    value: str = typer.Argument(
        ..., help="The string to be added to the ending of the filename."
    )
) -> None:
    "Adds a string to the ending of the filename."

    add_string_to_filename(value)


@app.command()
def upper() -> None:
    """Set the filename to uppercase."""

    current_file_paths = get_cwd_file_paths()
    current_filenames = []
    new_filenames = []

    for path in current_file_paths:
        name = path.stem
        extension = path.suffix

        if not name:
            continue

        new_name = name.upper()
        new_filenames.append(f"{new_name}{extension}")
        current_filenames.append(f"{name}{extension}")

    confirm_changes(current_filenames, new_filenames)


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
