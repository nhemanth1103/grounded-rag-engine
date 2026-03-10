from app.pipeline.rag_pipeline import build_vector_store, run_rag_query

# Build vector index
vector_store = build_vector_store("data/documents")

# Ask question
query = "What is the transformer architecture?"

answer, sources = run_rag_query(vector_store, query)

print("\nFinal Answer:\n")
print(answer)

print("\nFinal Answer:\n")
print(answer)