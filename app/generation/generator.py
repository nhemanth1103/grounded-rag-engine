from langchain_community.llms import Ollama
from app.config import settings


def generate_answer(query, retrieved_docs):
    """
    Generate an answer using the LLM based on retrieved documents.
    """

    llm = Ollama(model=settings.ollama_model)

    context = "\n\n".join([doc.page_content for doc in retrieved_docs])

    prompt = f"""
You are a helpful AI assistant.

Use the following context to answer the question.

Context:
{context}

Question:
{query}

Answer:
"""

    response = llm.invoke(prompt)

    return response