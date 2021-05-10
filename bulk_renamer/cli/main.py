import typer

app = typer.Typer()


@app.command()
def rename():
    print("Renaming files...")


if __name__ == "__main__":
    app()
