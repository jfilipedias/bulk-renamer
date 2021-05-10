import typer

app = typer.Typer()


@app.command()
def prefix():
    print("Calling add prefix command...")


@app.command()
def suffix():
    print("Calling add suffix command...")
