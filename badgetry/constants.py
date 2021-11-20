from typing import Dict

DEPENDENCIES_KEY: str = "tool.poetry.dependencies"
DEV_DEPENDENCIES_KEY: str = "tool.poetry.dev-dependencies"

PREDEFINED_BADGES: Dict[str, str] = {
    "bandit": (
        "[![security: bandit]"
        "(https://img.shields.io/badge/"
        "security-bandit-yellow.svg)]"
        "(https://github.com/PyCQA/bandit)"
    ),
    "black": (
        "[![Code style: black]"
        "(https://img.shields.io/badge/"
        "code%20style-black-000000.svg)]"
        "(https://github.com/psf/black)"
    ),
    "isort": (
        "[![Imports: isort]"
        "(https://img.shields.io/badge/"
        "%20imports-isort-%231674b1?style=flat&labelColor=ef8336)]"
        "(https://pycqa.github.io/isort/)"
    ),
}
