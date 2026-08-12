from pathlib import Path
from pydantic import BaseModel
from src.config_loader import load_environment_config


# =========================================================
# Application Settings
# =========================================================
class ApplicationSettings(BaseModel):
    name: str
    version: str
    environment: str


# =========================================================
# LLM Settings
# =========================================================
class LLMSettings(BaseModel):
    provider: str
    model: str
    temperature: float


# =========================================================
# Embedding Settings
# =========================================================
class EmbeddingSettings(BaseModel):
    provider: str
    model: str


# =========================================================
# Vector Database Settings
# =========================================================
class VectorDatabaseSettings(BaseModel):
    provider: str
    directory: str
    collection_name: str


# =========================================================
# Retrieval Settings
# =========================================================
class RetrievalSettings(BaseModel):
    top_k: int
    reranking: bool


# =========================================================
# Chunking Settings
# =========================================================
class ChunkingSettings(BaseModel):
    strategy: str
    chunk_size: int
    chunk_overlap: int


# =========================================================
# Logging Settings
# =========================================================
class LoggingSettings(BaseModel):
    level: str
    file: str


# =========================================================
# Main Settings
# =========================================================
class Settings(BaseModel):
    application: ApplicationSettings
    llm: LLMSettings
    embedding: EmbeddingSettings
    vector_database: VectorDatabaseSettings
    retrieval: RetrievalSettings
    chunking: ChunkingSettings
    logging: LoggingSettings


# =========================================================
# Project directories
# =========================================================
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = BASE_DIR / "config"

# =========================================================
# Select environment
# =========================================================
# Change this value to test different environments.
ENVIRONMENT = "development"

# =========================================================
# Load environment-specific configuration
# =========================================================
_CONFIG = load_environment_config(
    CONFIG_DIR,
    ENVIRONMENT,
)

# =========================================================
# Create validated Settings object
# =========================================================
settings = Settings(**_CONFIG)
