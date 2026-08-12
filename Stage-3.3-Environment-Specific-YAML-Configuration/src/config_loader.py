# this module contains functions to load and merge YAML configuration files for different environments.

from pathlib import Path
from typing import Any
import yaml


def load_yaml(file_path: Path) -> dict[str, Any]:
    """
    Load one YAML file and return its contents
    as a Python dictionary.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        # Convert YAML into a Python dictionary.
        config = yaml.safe_load(file)
    # Return an empty dictionary if the YAML file is empty.
    return config or {}


def merge_configs(
    base_config: dict[str, Any],
    override_config: dict[str, Any],
) -> dict[str, Any]:
    """
    Merge override_config into base_config.
    Nested dictionaries are merged recursively.
    """
    # Loop through every key in the override configuration.
    for key, value in override_config.items():
        # If both values are dictionaries,
        # merge them recursively.
        if (
            key in base_config
            and isinstance(base_config[key], dict)
            and isinstance(value, dict)
        ):
            merge_configs(base_config[key], value)
        else:
            # Otherwise the environment-specific value
            # replaces the base value.
            base_config[key] = value
    return base_config


def load_environment_config(
    config_dir: Path,
    environment: str,
) -> dict[str, Any]:
    """
    Load base.yaml and merge the selected
    environment configuration.
    """
    # Locate base configuration.
    base_file = config_dir / "base.yaml"
    # Locate environment-specific configuration.
    environment_file = config_dir / f"{environment}.yaml"
    # Make sure base.yaml exists.
    if not base_file.exists():
        raise FileNotFoundError(f"Base configuration not found: {base_file}")
    # Make sure the requested environment exists.
    if not environment_file.exists():
        raise FileNotFoundError(
            f"Environment configuration not found: " f"{environment_file}"
        )
    # Load base configuration.
    base_config = load_yaml(base_file)
    # Load environment-specific configuration.
    environment_config = load_yaml(environment_file)
    # Merge environment configuration over base configuration.
    return merge_configs(
        base_config,
        environment_config,
    )
