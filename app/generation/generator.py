from langchain_ollama import OllamaLLM
from app.config import settings
from app.generation.citation_formatter import format_sources



def generate_answer(query, retrieved_docs):
    """
    Standard answer generation (non-streaming)
    """

    llm = OllamaLLM(model=settings.ollama_model)

    context = "\n\n".join([doc.page_content for doc in retrieved_docs])

    prompt = f"""
You are a helpful AI assistant.

Use the provided context to answer the question.

Context:
{context}

Question:
{query}

Answer:
"""

    response = llm.invoke(prompt)

    return response


def stream_answer(query, retrieved_docs):
    """
    Streaming answer generation
    """

    llm = OllamaLLM(
        model=settings.ollama_model,
        streaming=True
    )

    context = "\n\n".join([doc.page_content for doc in retrieved_docs])

    prompt = f"""
You are a helpful AI assistant.

Use the provided context to answer the question.

Context:
{context}

Question:
{query}

Answer:
"""

    for token in llm.stream(prompt):
        yield token
