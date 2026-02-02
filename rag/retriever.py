from rag.vector_store import build_vector_store

def fetch_related_incidents(
    error_signals: list[str],
    historical_incidents: list[str],
    top_k: int = 2
) -> list[str]:
    """
    Retrieve semantically similar past incidents to improve RCA accuracy.
    """
    index = build_vector_store(historical_incidents)
    query_text = " ".join(error_signals)

    matches = index.similarity_search(query_text, k=top_k)
    return [match.page_content for match in matches]
