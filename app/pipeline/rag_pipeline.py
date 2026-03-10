from app.ingestion.loader import load_documents
from app.ingestion.chunker import chunk_documents
from app.embeddings.embedder import get_embedding_model
from app.vectorstore.store import create_vector_store
from app.retrieval.retriever import retrieve_documents
from app.generation.generator import generate_answer


def build_vector_store(data_path: str):
    """
    Build the vector database from documents.
    """

    print("\nLoading documents...")
    docs = load_documents(data_path)

    print(f"Loaded {len(docs)} documents")

    print("\nChunking documents...")
    chunks = chunk_documents(docs)

    print(f"Created {len(chunks)} chunks")

    print("\nLoading embedding model...")
    embedding_model = get_embedding_model()

    print("\nCreating vector database...")
    vector_store = create_vector_store(chunks, embedding_model)

    print("Vector database ready.")

    return vector_store


def run_rag_query(vector_store, query: str):
    """
    Execute a RAG query:
    retrieve relevant documents and generate an answer.
    """

    print("\nRetrieving relevant documents...")

    retrieved_docs = retrieve_documents(vector_store, query)

    print(f"Retrieved {len(retrieved_docs)} documents")

    print("\nGenerating answer with LLM...")

    answer = generate_answer(query, retrieved_docs)

    return answer, retrieved_docs