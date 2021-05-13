import re

import typer

from ..utils.functions import get_cwd_file_paths, rename_file


app = typer.Typer()

__doc__ = """Formats filename chars case based on the subcommands."""


@app.command()
def alternate() -> None:
    """Alternate the name characters between upper and lowercase."""

    paths = get_cwd_file_paths()

    for path in paths:
        name = path.stem
        extension = path.suffix

        if not name:
            continue

        formated_name = ""
        upper = True

        for char in name:
            formated_name += char.upper() if upper else char.lower()
            upper = not upper

        filename = f"{formated_name}{extension}"

        rename_file(path, filename)


@app.command()
def camel(
    whitespace: bool = typer.Option(
        False, "--whitespace", "-w", help="Maintains the filename whitespaces."
    )
) -> None:
    """Format the filename to camel case convention."""

    paths = get_cwd_file_paths()

    for path in paths:
        name = path.stem
        extension = path.suffix

        if not name:
            continue

        name = name.lower()
        name = name.title()
        name = name[:1].lower() + name[1:]

        if not whitespace:
            name = name.replace(" ", "")

        filename = f"{name}{extension}"

        rename_file(path, filename)


@app.command()
def lower() -> None:
    """Set the filename to lowercase."""

    paths = get_cwd_file_paths()

    for path in paths:
        name = path.stem
        extension = path.suffix

        if not name:
            continue

        name = name.lower()
        filename = f"{name}{extension}"

        rename_file(path, filename)


@app.command()
def kebab(
    upper: bool = typer.Option(
        False, "--upper", "-u", help="Set all characters to uppercase."
    )
) -> None:
    """Format the filename to kebab case convention."""

    paths = get_cwd_file_paths()

    for path in paths:
        name = path.stem
        extension = path.suffix

        if not name:
            continue

        name = name.upper() if upper else name.lower()
        name = re.sub("[^0-9a-zA-Z]+", "-", name)
        filename = f"{name}{extension}"

        rename_file(path, filename)


@app.command()
def pascal(
    whitespace: bool = typer.Option(
        False, "--whitespace", "-w", help="Maintains the filename whitespaces."
    )
) -> None:
    """Format the filename to pascal case convention."""

    paths = get_cwd_file_paths()

    for path in paths:
        name = path.stem
        extension = path.suffix

        if not name:
            continue

        name = name.title()

        if not whitespace:
            name = name.replace(" ", "")

        filename = f"{name}{extension}"

        rename_file(path, filename)


@app.command()
def upper() -> None:
    """Set the filename to uppercase."""

    paths = get_cwd_file_paths()

    for path in paths:
        name = path.stem
        extension = path.suffix

        if not name:
            continue

        name = name.upper()
        filename = f"{name}{extension}"

        rename_file(path, filename)


@app.command()
def snake(
    upper: bool = typer.Option(
        False, "--upper", "-u", help="Set all characters to uppercase."
    )
) -> None:
    """Format the filename to snake case convention."""

    paths = get_cwd_file_paths()

    for path in paths:
        name = path.stem
        extension = path.suffix

        if not name:
            continue

        name = name.upper() if upper else name.lower()
        name = re.sub("[^0-9a-zA-Z]+", "_", name)
        filename = f"{name}{extension}"

        rename_file(path, filename)
