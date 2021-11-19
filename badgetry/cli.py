import click
from scalpl import Cut

from . import __version__
from .constants import DEPENDENCIES_KEY
from .utils import load_toml


# More info:
# - https://click.palletsprojects.com/en/7.x/arguments/#file-path-arguments
# - https://click.palletsprojects.com/en/7.x/api/#click.Path
@click.command()
@click.argument(
    "input_path",
    type=click.Path(exists=True, file_okay=True, dir_okay=False),
    default="./pyproject.toml",
)
@click.version_option(version=__version__)
def main(input_path):
    """A Python package to generate metadata badges from Poetry's pyproject.toml files."""
    metadata = load_toml(input_path)
    # pretty_print(metadata)

    proxy = Cut(metadata)
    # pretty_print(proxy.data)

    deps = proxy[DEPENDENCIES_KEY].keys()
    click.echo(deps)
