import typer

from bulk_renamer.functions import confirm_changes, get_cwd_file_paths, get_value_input

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
    value: str = typer.Option(
        "", help="The string to be added to the beginning of the filename."
    )
) -> None:
    "Adds a string to the beginning of the filename."

    add_affix_to_filename(value)


@app.command()
def remove(
    value: str = typer.Argument(..., help="The string to remove from filename.")
) -> None:
    """Remove a specified string from the filename."""

    current_file_paths = get_cwd_file_paths()
    current_filenames = []
    new_filenames = []

    if not value:
        value = get_value_input("What's the string you want to remove: ")[0]

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
    old_value: str = typer.Option("", help="The string to shearch for."),
    new_value: str = typer.Option("", help="The string to replace the old value with."),
) -> None:
    """Replaces a specified string in the filename with another specified string."""

    if not old_value and not new_value:
        new_value, old_value = get_value_input(
            new_value_message="What's the new value you want to put:",
            old_value_message="What's the old value you want to replace:",
        )
    elif not old_value:
        old_value = get_value_input(
            new_value_message="",
            old_value_message="What's the string you want to remove:",
        )[1]
    elif not new_value:
        new_value = get_value_input("What's the string you want to put:")[0]

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
    value: str = typer.Option(
        "", help="The string to be added to the ending of the filename."
    )
) -> None:
    "Adds a string to the ending of the filename."

    add_affix_to_filename(value, is_prefix=False)


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


def add_affix_to_filename(value: str = "", is_prefix: bool = True) -> None:
    """Adds a affix to a filename."""

    if not value:
        affix = "prefix" if is_prefix else "suffix"
        value = get_value_input(f"What's the {affix} you want to add:")[0]

    current_file_paths = get_cwd_file_paths()
    current_filenames = []
    new_filenames = []

    for path in current_file_paths:
        name = path.stem
        extension = path.suffix

        if not name:
            continue

        new_name = f"{value}{name}" if is_prefix else f"{name}{value}"
        new_filenames.append(f"{new_name}{extension}")
        current_filenames.append(f"{name}{extension}")

    confirm_changes(current_filenames, new_filenames)
