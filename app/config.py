import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field


# Load environment variables from .env
load_dotenv()


class Settings(BaseModel):
    # Models
    ollama_model: str = Field(default=os.getenv("OLLAMA_MODEL"))
    embed_model: str = Field(default=os.getenv("EMBED_MODEL"))

    # Vector DB
    chroma_path: str = Field(default=os.getenv("CHROMA_PATH"))

    # Retrieval
    top_k: int = Field(default=int(os.getenv("TOP_K", 3)))
    similarity_threshold: float = Field(
        default=float(os.getenv("SIMILARITY_THRESHOLD", 0.7))
    )

    # Chunking
    chunk_size: int = Field(default=int(os.getenv("CHUNK_SIZE", 500)))
    chunk_overlap: int = Field(default=int(os.getenv("CHUNK_OVERLAP", 80)))

    # Context Management
    max_context_tokens: int = Field(
        default=int(os.getenv("MAX_CONTEXT_TOKENS", 1500))
    )


settings = Settings()