def format_sources(retrieved_docs):
    """
    Format retrieved document metadata into readable citations.
    """

    sources = []

    for doc in retrieved_docs:
        source = doc.metadata.get("source", "Unknown Source")
        page = doc.metadata.get("page") or doc.metadata.get("page_number")

        citation = f"{source} (Page {page})"

        if citation not in sources:
            sources.append(citation)

    return sources