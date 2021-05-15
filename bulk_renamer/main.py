import typer

import bulk_renamer.commands as commands

__doc__ = """Bulk Renamer is a CLI to help you to easily rename a
list of files. You just need to run the commands from the folder that contains
the files you want to rename.
"""

app = typer.Typer(help=__doc__)

app.command()(commands.alternate)
app.command()(commands.camel)
app.command()(commands.lower)
app.command()(commands.kebab)
app.command()(commands.pascal)
app.command()(commands.prefix)
app.command()(commands.remove)
app.command()(commands.replace)
app.command()(commands.snake)
app.command()(commands.suffix)
app.command()(commands.upper)
