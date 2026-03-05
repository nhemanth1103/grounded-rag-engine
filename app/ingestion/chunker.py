from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from app.config import settings


def chunk_documents(documents: List[Document]) -> List[Document]:
    """
    Split documents into smaller chunks suitable for embeddings.
    Uses recursive character splitting with overlap.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
        separators=["\n\n", "\n", " ", ""],
    )

    chunks = text_splitter.split_documents(documents)

    return chunks