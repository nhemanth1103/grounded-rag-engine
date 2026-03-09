def retrieve_documents(vector_store, query, k=4):
    """
    Retrieve top-k relevant document chunks for a query.
    """

    results = vector_store.similarity_search(
        query=query,
        k=k
    )

    return results