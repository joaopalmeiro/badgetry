from pathlib import Path

import click

from . import __version__
from .utils import load_toml


@click.command()
@click.version_option(version=__version__)
def main():
    """A Python package to generate metadata badges from Poetry's pyproject.toml files."""
    metadata = load_toml(Path("pyproject.toml"))
    click.echo(metadata)
