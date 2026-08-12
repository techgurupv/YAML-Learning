from pathlib import Path

# from config_loader import load_all_configs
from src.config_loader import load_all_configs

# Find the root directory of our project.
BASE_DIR = Path(__file__).resolve().parent.parent

# Location containing all YAML configuration files.
CONFIG_DIR = BASE_DIR / "config"


# Load and combine all YAML configuration files.
# this makes a call to the below function from another module,
# which is responsible for loading and merging all the YAML configuration 
# files in the specified directory into a single Python dictionary.
# The resulting dictionary is then stored in the _CONFIG variable for easy access
# to the configuration values throughout the application.
_CONFIG = load_all_configs(CONFIG_DIR)

# once you have read all the configuration files and merged them into a single dictionary,
# you can access the individual configuration values using the appropriate keys like below.
# Application configuration
APPLICATION_NAME = _CONFIG["application"]["name"]
APPLICATION_VERSION = _CONFIG["application"]["version"]
ENVIRONMENT = _CONFIG["application"]["environment"]

# LLM configuration
LLM_PROVIDER = _CONFIG["llm"]["provider"]
LLM_MODEL = _CONFIG["llm"]["model"]
LLM_TEMPERATURE = _CONFIG["llm"]["temperature"]

# Embedding configuration
EMBEDDING_PROVIDER = _CONFIG["embedding"]["provider"]
EMBEDDING_MODEL = _CONFIG["embedding"]["model"]

# Vector database configuration
VECTOR_DB_PROVIDER = _CONFIG["vector_database"]["provider"]
CHROMA_DB_DIRECTORY = _CONFIG["vector_database"]["directory"]
COLLECTION_NAME = _CONFIG["vector_database"]["collection_name"]

# Retrieval configuration
TOP_K = _CONFIG["retrieval"]["top_k"]
RERANKING_ENABLED = _CONFIG["retrieval"]["reranking"]

# Chunking configuration
CHUNKING_STRATEGY = _CONFIG["chunking"]["strategy"]
CHUNKING_SIZE = _CONFIG["chunking"]["chunk_size"]
CHUNKING_OVERLAP = _CONFIG["chunking"]["chunk_overlap"]

# Logging configuration
LOG_LEVEL = _CONFIG["logging"]["level"]
LOG_FILE = _CONFIG["logging"]["file"]
