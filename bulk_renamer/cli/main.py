import typer

from . import add, case

app = typer.Typer()

commands = [add, case]

for command in commands:
    app.add_typer(
        command.app, name=command.__name__.split(".")[-1], help=command.__doc__
    )


@app.command()
def remove():
    print("Calling remove command...")


@app.command()
def rename():
    print("Calling rename command...")


@app.command()
def substitute():
    print("Calling substitute command...")
