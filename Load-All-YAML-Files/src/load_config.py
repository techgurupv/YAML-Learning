# this file is used to load all the configuration files in the config directory and print the values of the
# keys in the config dictionary
from pathlib import Path
from yaml_loader import load_yaml

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = BASE_DIR / "config"

# Load all YAML configuration files in the config directory and return a dictionary of configurations
def load_all_configs(config_dir):
    
    config_dir = Path(config_dir)
    if not config_dir.exists():
        raise FileNotFoundError(f"Configuration directory not found: {config_dir}")
    configs = {} # Initialize an empty dictionary to hold the configurations that have been fetched from the YAML files
    # Get a list of all YAML files in the configuration directory
    yaml_files = list(config_dir.glob("*.yaml"))
    # print the list of YAML files found in the configuration directory
    print(yaml_files)
    print('Number Of YAML files found:', len(yaml_files))
    
    # Check if any YAML files were found, and raise an error if none were found
    if not yaml_files:
        raise FileNotFoundError(f"No YAML configuration files found in: {config_dir}")
    for config_file in yaml_files:
        config = load_yaml(config_file)
        if not isinstance(config, dict):
            raise ValueError(f"Configuration must be a dictionary: {config_file}")
        configs.update(config)
    return configs


# enable this code to test the load_all_configs function and print the values of the keys in the config dictionary
# config = load_all_configs(CONFIG_DIR)
# print(config["application"]["name"])
# print(config["llm"]["model"])
# print(config["embedding"]["model"])
# print(config["vector_database"]["collection_name"])
# print(config["retrieval"]["top_k"])
# print(config["chunking"]["strategy"])
# print(config["chunking"]["chunk_size"])
# print(config["chunking"]["chunk_overlap"])
