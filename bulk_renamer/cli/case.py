import typer

app = typer.Typer()


@app.command()
def alternate():
    print("Calling case alternate command...")


@app.command()
def camel():
    print("Calling case camel command...")


@app.command()
def lower():
    print("Calling case lower command...")


@app.command()
def pascal():
    print("Calling case pascal command...")


@app.command()
def upper():
    print("Calling case upper command...")


@app.command()
def snake():
    print("Calling case snake command...")
