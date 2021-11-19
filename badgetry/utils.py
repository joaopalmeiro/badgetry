import json

import click
import toml


def load_toml(input_path):
    with open(input_path, "r") as f:
        content = toml.load(f)

    return content


def pretty_print(data):
    click.echo(json.dumps(data, ensure_ascii=False, sort_keys=False, indent=2))
