from pathlib import Path
from typing import Any

import yaml


def load_yaml(file_path: str | Path) -> dict[str, Any]:
    """
    Read a YAML file and return its contents
    as a Python dictionary.
    """

    # Convert the incoming path into a Path object.
    file_path = Path(file_path)

    # Make sure the requested YAML file exists.
    if not file_path.exists():
        raise FileNotFoundError(
            f"YAML configuration file not found: {file_path}"
        )

    # Open the YAML file using UTF-8 encoding.
    with open(file_path, "r", encoding="utf-8") as file:

        # Convert YAML into a Python dictionary.
        config = yaml.safe_load(file)

    # Protect against an empty YAML file.
    if config is None:
        raise ValueError(
            f"YAML configuration file is empty: {file_path}"
        )

    return config