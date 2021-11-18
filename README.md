# badgetry

[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

A Python package to generate metadata badges from Poetry's `pyproject.toml` files.

## Development

- `poetry install`
- `poetry shell`

## Tech Stack

- [Click](https://click.palletsprojects.com/) (for the interface)
- [toml](https://github.com/uiri/toml) (to parse TOML files)

### Packaging and Development

- [Poetry](https://python-poetry.org/)
- [Mypy](http://mypy-lang.org/)
- [isort](https://pycqa.github.io/isort/)
- [Black](https://github.com/psf/black)
- [Flake8](https://flake8.pycqa.org/)
  - [flake8-bugbear](https://github.com/PyCQA/flake8-bugbear)
  - [flake8-comprehensions](https://github.com/adamchainz/flake8-comprehensions)
  - [pep8-naming](https://github.com/PyCQA/pep8-naming)
  - [flake8-builtins](https://github.com/gforcada/flake8-builtins)
- [Bandit](https://bandit.readthedocs.io/)

This CLI was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [`joaopalmeiro/cookiecutter-templates/python-cli`](https://github.com/joaopalmeiro/cookiecutter-templates) project template.

## Notes

- [Easy Way to Create CLI Scripts with JavaScript and Node](https://youtu.be/dfTpFFZwazI) by James Q Quick.
- [create-node-cli](https://github.com/ahmadawais/create-node-cli): CRA-like CLI to create Node.js CLI applications.
- [node-cli-boilerplate](https://github.com/sindresorhus/node-cli-boilerplate).
- [`bin`](https://docs.npmjs.com/cli/v8/configuring-npm/package-json#bin) (`package.json` file): command to use the CLI (similar to the `[tool.poetry.scripts]` section of the `pyproject.toml` file).
