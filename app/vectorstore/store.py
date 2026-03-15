import os
from langchain_community.vectorstores import Chroma
from app.config import settings


def create_vector_store(chunks, embedding_model):
    """
    Create or load the Chroma vector database.
    """

    persist_directory = settings.chroma_path

    # If database already exists, load it
    if os.path.exists(persist_directory) and os.listdir(persist_directory):
        print("\nLoading existing vector database...")

        vector_store = Chroma(
            persist_directory=persist_directory,
            embedding_function=embedding_model
        )

    else:
        print("\nCreating new vector database...")

        vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=embedding_model,
            persist_directory=persist_directory
        )

        vector_store.persist()

    return vector_store