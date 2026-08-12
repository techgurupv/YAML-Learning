from pathlib import Path
from typing import Any
from .config_loader import load_all_configs


# =========================================================
# LLM configuration
# =========================================================
class LLMSettings:
    def __init__(self, config: dict[str, Any]):
        # Store the LLM provider.
        self.provider = config["provider"]
        # Store the LLM model name.
        self.model = config["model"]
        # Store the temperature used by the LLM.
        self.temperature = config["temperature"]


# =========================================================
# Embedding configuration
# =========================================================
class EmbeddingSettings:
    def __init__(self, config: dict[str, Any]):
        # Embedding provider.
        self.provider = config["provider"]
        # Embedding model.
        self.model = config["model"]


# =========================================================
# Vector database configuration
# =========================================================
class VectorDatabaseSettings:
    def __init__(self, config: dict[str, Any]):
        # Vector database provider.
        self.provider = config["provider"]
        # Database directory.
        self.directory = config["directory"]
        # Collection name.
        self.collection_name = config["collection_name"]


# =========================================================
# Retrieval configuration
# =========================================================
class RetrievalSettings:
    def __init__(self, config: dict[str, Any]):
        # Number of documents to retrieve.
        self.top_k = config["top_k"]
        # Whether reranking is enabled.
        self.reranking = config["reranking"]


# =========================================================
# Chunking configuration
# =========================================================
class ChunkingSettings:
    def __init__(self, config: dict[str, Any]):
        # Chunking strategy.
        self.strategy = config["strategy"]
        # Number of characters/tokens used per chunk,
        # depending on the splitter implementation.
        self.chunk_size = config["chunk_size"]
        # Number of overlapping characters/tokens.
        self.chunk_overlap = config["chunk_overlap"]


# =========================================================
# Application configuration
# =========================================================
class ApplicationSettings:
    def __init__(self, config: dict[str, Any]):
        # Application name.
        self.name = config["name"]
        # Application version.
        self.version = config["version"]
        # Current environment.
        self.environment = config["environment"]


# =========================================================
# Logging configuration
# =========================================================
class LoggingSettings:
    def __init__(self, config: dict[str, Any]):
        # Logging level.
        self.level = config["level"]
        # Logging output file.
        self.file = config["file"]


# =========================================================
# Main Settings object
# =========================================================
class Settings:
    def __init__(self, config: dict[str, Any]):
        # Convert each YAML section into a dedicated
        # configuration object.
        self.application = ApplicationSettings(config["application"])
        self.llm = LLMSettings(config["llm"])
        self.embedding = EmbeddingSettings(config["embedding"])
        self.vector_database = VectorDatabaseSettings(config["vector_database"])
        self.retrieval = RetrievalSettings(config["retrieval"])
        self.chunking = ChunkingSettings(config["chunking"])
        self.logging = LoggingSettings(config["logging"])


# =========================================================
# Locate project root
# =========================================================
BASE_DIR = Path(__file__).resolve().parent.parent
# =========================================================
# Locate configuration directory
# =========================================================
CONFIG_DIR = BASE_DIR / "config"
# =========================================================
# Load all YAML files
# =========================================================
_CONFIG = load_all_configs(CONFIG_DIR)
# =========================================================
# Create one global Settings object
# =========================================================
settings = Settings(_CONFIG)
