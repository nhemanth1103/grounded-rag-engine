from fastapi import FastAPI
from pydantic import BaseModel

from app.pipeline.rag_pipeline import build_vector_store, run_rag_query

app = FastAPI()

vector_store = build_vector_store("data/documents")


class QueryRequest(BaseModel):
    question: str


@app.get("/")
def health():
    return {"status": "RAG system running"}


@app.post("/ask")
def ask_question(request: QueryRequest):

    answer, _ = run_rag_query(vector_store, request.question)

    return {
        "question": request.question,
        "answer": answer
    }