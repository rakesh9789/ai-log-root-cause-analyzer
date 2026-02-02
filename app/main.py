from fastapi import FastAPI, UploadFile
from core.log_parser import extract_error_signals
from core.rca_agent import generate_rca_report
from core.confidence import compute_confidence_score
from rag.retriever import fetch_related_incidents

app = FastAPI(title="AI Log Root Cause Analyzer")

@app.post("/analyze-log")
async def analyze_log(file: UploadFile):
    raw_logs = (await file.read()).decode("utf-8")

    error_signals = extract_error_signals(raw_logs)

    with open("data/known_issues.txt") as f:
        historical_incidents = f.readlines()

    related_incidents = fetch_related_incidents(
        error_signals,
        historical_incidents
    )

    rca_report = generate_rca_report(
        error_signals,
        related_incidents
    )

    confidence_score = compute_confidence_score(
        error_signals,
        related_incidents
    )

    return {
        "error_signals": error_signals,
        "rca_report": rca_report,
        "confidence_score": confidence_score,
        "related_incidents": related_incidents
    }
