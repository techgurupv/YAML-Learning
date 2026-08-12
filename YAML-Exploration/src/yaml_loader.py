from pathlib import Path
from typing import Any

import yaml


def load_yaml(file_path: str | Path) -> dict[str, Any]:

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"YAML configuration file not found: {file_path}"
        )

    with open(file_path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    if config is None:
        raise ValueError(
            f"YAML configuration file is empty: {file_path}"
        )

    return config