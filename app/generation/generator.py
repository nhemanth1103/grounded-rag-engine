from langchain_community.llms import Ollama
from app.config import settings
from app.generation.citation_formatter import format_sources


def generate_answer(query, retrieved_docs):

    llm = Ollama(model=settings.ollama_model)

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

    sources = format_sources(retrieved_docs)

    final_output = f"{response}\n\nSources:\n"

    for src in sources:
        final_output += f"- {src}\n"

    return final_output