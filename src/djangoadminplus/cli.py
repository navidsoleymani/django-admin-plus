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
def startproject(projectname: str):
    from pathlib import Path
    root_path = Path(__file__).resolve().parent

    os.system(f'django-admin startproject {projectname}')
    os.system(f'rm -r {projectname}/{projectname}')
    os.system(f'cp -r {root_path}/repo/conf {projectname}')
    os.system(f'cp -r {root_path}/repo/root/* {projectname}')
    os.system(f'cp {root_path}/repo/root/.env {projectname}')
    os.system(f'cp {root_path}/repo/root/.gitignore {projectname}')
    os.system(f"cd {projectname} && git init && git add -A && git commit -m 'init'")
    os.system(f'mv venv {projectname}')

