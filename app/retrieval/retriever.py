def retrieve_documents(vector_store, query, k=4):
    """
    Retrieve relevant document chunks using MMR (Max Marginal Relevance).
    """

    results = vector_store.max_marginal_relevance_search(
        query=query,
        k=k,
        fetch_k=10
    )

    return results