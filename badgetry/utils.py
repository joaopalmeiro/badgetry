import toml


def load_toml(input_path):
    with open(input_path, "r") as f:
        content = toml.load(f)

    return content
