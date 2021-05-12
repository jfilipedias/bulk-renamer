import typer

from . import add, case, cmd

app = typer.Typer()

commands = [add, case]

for command in commands:
    app.add_typer(
        command.app, name=command.__name__.split(".")[-1], help=command.__doc__
    )

app.command()(cmd.remove)
app.command()(cmd.rename)
app.command()(cmd.replace)
