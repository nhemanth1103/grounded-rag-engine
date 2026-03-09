from langchain_community.vectorstores import Chroma
from app.config import settings


def create_vector_store(chunks, embedding_model):
    """
    Create a Chroma vector database from document chunks.
    """

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=settings.chroma_path
    )

    return vector_store