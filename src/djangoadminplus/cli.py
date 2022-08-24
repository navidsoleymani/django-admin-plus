from typing import Optional
import sys
import os
import typer

from . import __app_name__, __version__

app = typer.Typer()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f'{__app_name__} v{__version__}')
        raise typer.Exit()


@app.callback()
def main(
        version: Optional[bool] = typer.Option(
            None,
            '--version',
            '-v',
            help="Show the application's version and exit.",
            callback=_version_callback,
            is_eager=True,
        )
) -> None:
    return


@app.command()
def startproject():
    from pathlib import Path
    root_path = Path(__file__).resolve().parent

    os.system(f'django-admin startproject projectname')
    os.system(f'cp -r projectname/manage.py .')
    os.system(f'rm -r projectname')
    os.system(f'cp -r {root_path}/repo/conf .')
    os.system(f'cp -r {root_path}/repo/root/* .')
    os.system(f'cp {root_path}/repo/root/.env .')
    os.system(f'cp {root_path}/repo/root/.gitignore .')
    os.system(f"cd git init && git add -A && git commit -m 'init'")
