from app.config import settings
from app.ingestion.loader import load_documents
from app.ingestion.chunker import chunk_documents
from app.embeddings.embedder import get_embedding_model
from app.vectorstore.store import create_vector_store
from app.embeddings.embedder import get_embedding_model
from app.retrieval.retriever import retrieve_documents

# --- Config check ---
print("Loaded Model:", settings.ollama_model)
print("Embedding Model:", settings.embed_model)
print("Chroma Path:", settings.chroma_path)

# --- Loader test ---
docs = load_documents("data/documents")

print(f"\nLoaded {len(docs)} pages")

if docs:
    print("Source:", docs[0].metadata.get("source"))
    print("Page:", docs[0].metadata.get("page_number"))
    print("Preview:", docs[0].page_content[:200])

# --- Chunking test ---
chunks = chunk_documents(docs)

print(f"\nCreated {len(chunks)} chunks")

if chunks:
    print("First chunk preview:")
    print(chunks[0].page_content[:200])

# --- Embedding test --
embedding_model = get_embedding_model()

vector = embedding_model.embed_query(chunks[0].page_content)

print("\nEmbedding vector length:", len(vector))

embedding_model = get_embedding_model()

vector_store = create_vector_store(chunks, embedding_model)

print("\nVector database created successfully.")

query = "What is the transformer architecture?"

results = retrieve_documents(vector_store, query)

print("\nRetrieved Documents:")

for i, doc in enumerate(results):
    print(f"\nResult {i+1}")
    print("Source:", doc.metadata.get("source"))
    print("Page:", doc.metadata.get("page"))
    print("Text:", doc.page_content[:200])