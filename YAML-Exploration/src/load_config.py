from pathlib import Path
from yaml_loader import load_yaml

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = BASE_DIR / "config"

app_config = load_yaml(
    CONFIG_DIR / "app.yaml"
)
llm_config = load_yaml(
    CONFIG_DIR / "llm.yaml"
)
embedding_config = load_yaml(
    CONFIG_DIR / "embedding.yaml"
)
vector_database_config = load_yaml(
    CONFIG_DIR / "vector_database.yaml"
)
retrieval_config = load_yaml(
    CONFIG_DIR / "retrieval.yaml"
)
config = {
    **app_config,
    **llm_config,
    **embedding_config,
    **vector_database_config,
    **retrieval_config
}
# The ** means:
# Unpack the dictionary's key/value pairs into another dictionary.

print(config["application"]["name"])
print(config["llm"]["model"])
print(config["embedding"]["model"])
print(config["vector_database"]["collection_name"])
print(config["retrieval"]["top_k"])

# config/
#     │
#     ├── app.yaml
#     ├── llm.yaml
#     ├── embedding.yaml
#     ├── vector_database.yaml
#     └── retrieval.yaml

        #             YAML
        #               │
        #   ┌───────────┼────────────┐
        #   ↓           ↓            ↓
        # llm.yaml  embedding.yaml retrieval.yaml
        #   │           │            │
        #   └───────────┼────────────┘
        #               ↓
        #          settings.py
        #               ↓
        #        Settings object
        #               ↓
        #      Enterprise RAG