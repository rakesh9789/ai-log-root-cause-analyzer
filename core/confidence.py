def compute_confidence_score(
    error_signals: list[str],
    related_incidents: list[str]
) -> float:
    """
    Confidence is higher when current errors match known incidents.
    This keeps scoring explainable and interview-friendly.
    """
    if not error_signals:
        return 0.0

    base_confidence = 0.5
    similarity_boost = min(len(related_incidents) * 0.15, 0.4)

    final_score = base_confidence + similarity_boost
    return round(min(final_score, 0.95), 2)
