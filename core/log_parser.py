ERROR_INDICATORS = ["error", "exception", "traceback", "failed"]

def extract_error_signals(raw_logs: str) -> list[str]:
    """
    Extract only meaningful error-related lines from noisy logs.
    This helps the LLM focus on failure signals instead of INFO spam.
    """
    log_lines = raw_logs.splitlines()
    error_signals = []

    for line in log_lines:
        if any(keyword in line.lower() for keyword in ERROR_INDICATORS):
            error_signals.append(line.strip())

    return error_signals
