import typer

from . import add, case, cmd

BULK_RENAMER_HELP = """Bulk Renamer is a CLI to help you to easily rename a
list of files. You just need to run the commands from the folder that contains
the files you want to
rename.
"""

app = typer.Typer(help=BULK_RENAMER_HELP)

commands = [add, case]

for command in commands:
    app.add_typer(
        command.app, name=command.__name__.split(".")[-1], help=command.__doc__
    )

app.command()(cmd.remove)
app.command()(cmd.replace)
