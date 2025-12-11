import typer
from ceaser import ceaser
from atbash import atbash
from cb55 import cb55

app = typer.Typer()

app.command()(ceaser)
app.command()(atbash)
app.command()(cb55)

if __name__ == "__main__":
    app()