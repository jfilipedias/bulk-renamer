import re

import typer

from ..utils.functions import get_cwd_file_paths, confirm_changes


app = typer.Typer()

__doc__ = """Formats filename chars case based on the subcommands."""


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
            new_name = re.sub("[^0-9a-zA-Z]+", "", new_name)

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
        new_name = re.sub("[^0-9a-zA-Z]+", "-", new_name)
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
            new_name = re.sub("[^0-9a-zA-Z]+", "", new_name)

        new_filenames.append(f"{new_name}{extension}")
        current_filenames.append(f"{name}{extension}")

    confirm_changes(current_filenames, new_filenames)


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
        new_name = re.sub("[^0-9a-zA-Z]+", "_", new_name)
        new_filenames.append(f"{new_name}{extension}")
        current_filenames.append(f"{name}{extension}")

    confirm_changes(current_filenames, new_filenames)
