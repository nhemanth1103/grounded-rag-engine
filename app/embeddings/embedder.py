from langchain_ollama import OllamaEmbeddings
from app.config import settings


def get_embedding_model():
    """
    Initialize Ollama embedding model.
    """

    embeddings = OllamaEmbeddings(
        model=settings.embed_model
    )

    return embeddings