from app.config import settings
from app.ingestion.loader import load_documents
from app.ingestion.chunker import chunk_documents
from app.embeddings.embedder import get_embedding_model

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