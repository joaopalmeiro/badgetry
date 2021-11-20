import click
from scalpl import Cut

from . import __version__
from .constants import DEPENDENCIES_KEY, DEV_DEPENDENCIES_KEY, PREDEFINED_BADGES
from .utils import list2str, load_toml


# More info:
# - https://click.palletsprojects.com/en/7.x/arguments/#file-path-arguments
# - https://click.palletsprojects.com/en/7.x/api/#click.Path
# - https://click.palletsprojects.com/en/8.0.x/documentation/#documenting-arguments
@click.command()
@click.argument(
    "input_path",
    type=click.Path(exists=True, file_okay=True, dir_okay=False),
    default="./pyproject.toml",
)
@click.version_option(version=__version__)
def main(input_path):
    """A Python package to generate metadata badges from Poetry's pyproject.toml files.

    INPUT_PATH matches the pyproject.toml file in the current folder by default.
    """
    metadata = load_toml(input_path)
    # pretty_print(metadata)

    proxy = Cut(metadata)
    # pretty_print(proxy.data)

    deps = proxy[DEPENDENCIES_KEY]
    dev_deps = proxy[DEV_DEPENDENCIES_KEY]
    all_deps = {**deps, **dev_deps}
    # click.echo(all_deps)

    badges = [PREDEFINED_BADGES[d] for d in PREDEFINED_BADGES if d in all_deps]
    # pretty_print(badges)

    if badges:
        output = list2str(badges)
        click.echo(output)
    else:
        click.secho("No badges", fg="red")
