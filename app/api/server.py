from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from app.pipeline.rag_pipeline import stream_rag_query

from app.pipeline.rag_pipeline import build_vector_store, run_rag_query

app = FastAPI()

vector_store = build_vector_store("data/documents")


class QueryRequest(BaseModel):
    question: str


@app.get("/")
def health():
    return {"status": "RAG system running"}




@app.post("/ask")
def ask(request: QueryRequest):

    answer, _ = run_rag_query(vector_store, request.question)

    return {
        "answer": str(answer)
    }


@app.post("/ask-stream")
def ask_stream(request: QueryRequest):

    def generate():
        for token in stream_rag_query(vector_store, request.question):
            yield token

    return StreamingResponse(generate(), media_type="text/plain")