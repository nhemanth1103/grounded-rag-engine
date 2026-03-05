from pathlib import Path
from typing import List
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


def load_documents(data_dir: str) -> List[Document]:
    documents = []

    pdf_files = Path(data_dir).glob("*.pdf")

    for pdf in pdf_files:
        loader = PyPDFLoader(str(pdf))
        pages = loader.load()

        for i, page in enumerate(pages):
            page.metadata["source"] = pdf.name
            page.metadata["page_number"] = i + 1  # human-readable page

        documents.extend(pages)

    return documents