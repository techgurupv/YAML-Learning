from pathlib import Path
from pydantic import BaseModel
from src.config_loader import load_all_configs


# =========================================================
# Application Settings
# =========================================================
class ApplicationSettings(BaseModel):
    # Application name must be a string.
    name: str
    # Application version must be a string.
    version: float
    # Environment must be a string.
    environment: str


# =========================================================
# LLM Settings
# =========================================================
class LLMSettings(BaseModel):
    # LLM provider, for example Groq.
    provider: str
    # LLM model name.
    model: str
    # Temperature must be a floating-point number.
    temperature: float


# =========================================================
# Embedding Settings
# =========================================================
class EmbeddingSettings(BaseModel):
    # Embedding provider.
    provider: str
    # Embedding model.
    model: str


# =========================================================
# Vector Database Settings
# =========================================================
class VectorDatabaseSettings(BaseModel):
    # Vector database provider.
    provider: str
    # Database directory.
    directory: str
    # Collection name.
    collection_name: str


# =========================================================
# Retrieval Settings
# =========================================================
class RetrievalSettings(BaseModel):
    # Number of documents to retrieve.
    top_k: int
    # Whether reranking is enabled.
    reranking: bool


# =========================================================
# Chunking Settings
# =========================================================
class ChunkingSettings(BaseModel):
    # Chunking strategy.
    strategy: str
    # Size of each chunk.
    chunk_size: int
    # Number of overlapping characters/tokens.
    chunk_overlap: int


# =========================================================
# Logging Settings
# =========================================================
class LoggingSettings(BaseModel):
    # Logging level.
    level: str
    # Logging file path.
    file: str


# =========================================================
# Main Settings
# =========================================================
class Settings(BaseModel):
    # Application configuration.
    application: ApplicationSettings
    # LLM configuration.
    llm: LLMSettings
    # Embedding configuration.
    embedding: EmbeddingSettings
    # Vector database configuration.
    vector_database: VectorDatabaseSettings
    # Retrieval configuration.
    retrieval: RetrievalSettings
    # Chunking configuration.
    chunking: ChunkingSettings
    # Logging configuration.
    logging: LoggingSettings


# =========================================================
# Locate project root
# =========================================================
# __file__ = src/settings.py
#
# parent      = src/
# parent.parent = project root
BASE_DIR = Path(__file__).resolve().parent.parent
# =========================================================
# Locate configuration directory
# =========================================================
CONFIG_DIR = BASE_DIR / "config"
# =========================================================
# Load all YAML configuration files
# =========================================================
# This returns one combined Python dictionary.
_CONFIG = load_all_configs(CONFIG_DIR)
# =========================================================
# Create validated Settings object
# =========================================================
# Pydantic validates the entire configuration here.
settings = Settings(**_CONFIG)
