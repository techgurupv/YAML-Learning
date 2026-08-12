from pathlib import Path
from typing import Any

from src.yaml_loader import load_yaml


def load_all_configs(config_dir: str | Path) -> dict[str, Any]:
    """
    Discover all YAML files in the configuration directory
    and merge them into one Python dictionary.
    """

    # Convert the directory path into a Path object.
    config_dir = Path(config_dir)

    # Make sure the configuration directory exists.
    if not config_dir.exists():
        raise FileNotFoundError(f"Configuration directory not found: {config_dir}")

    # Start with an empty dictionary.
    configs = {}

    # Find every .yaml file in the configuration directory.
    for config_file in config_dir.glob("*.yaml"):

        # Load the individual YAML file.
        config = load_yaml(config_file)

        # Make sure each YAML file contains a dictionary.
        if not isinstance(config, dict):
            raise ValueError(f"Configuration must be a dictionary: {config_file}")

        # Add the configuration to the combined dictionary.
        configs.update(config)

    # Make sure at least one YAML file was found.
    if not configs:
        raise ValueError(f"No configuration found in: {config_dir}")

    # finally return the full configuration that has been loaded from all the YAML files in the specified 
    # directory.
    return configs
