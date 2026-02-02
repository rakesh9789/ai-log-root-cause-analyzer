from langchain_community.llms import Ollama
from core.prompt import build_rca_prompt

llm = Ollama(model="llama3")

def generate_rca_report(
    error_signals: list[str],
    related_incidents: list[str]
) -> str:
    """
    Generate a human-readable RCA report using LLM reasoning.
    """
    prompt = build_rca_prompt(error_signals, related_incidents)
    return llm.invoke(prompt)
