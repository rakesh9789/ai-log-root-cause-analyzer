def build_rca_prompt(
    error_signals: list[str],
    related_incidents: list[str]
) -> str:
    """
    Prompt designed to simulate how an engineer reasons about
    production failures using logs and past incidents.
    """
    return f"""
We are investigating a production issue based on application logs.

Below are the error signals extracted from the logs, followed by
similar incidents that have occurred in the past.

Error signals:
{error_signals}

Related historical incidents:
{related_incidents}

Based on this information:
- Determine the most likely root cause
- Explain what led to the failure
- Outline concrete steps to fix the issue
- Suggest preventive actions to avoid recurrence

Please keep the explanation practical and easy to follow,
as if writing an internal incident analysis report.
"""
