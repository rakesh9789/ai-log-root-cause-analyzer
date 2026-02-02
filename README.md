# AI Log Root Cause Analyzer

I built this project to simulate how engineers debug real production
issues using AI-assisted analysis.

The system processes application logs, extracts failure signals,
retrieves similar historical incidents using Retrieval Augmented
Generation (RAG), and generates a root cause analysis with
confidence scoring.

## Key Capabilities
- Parses noisy production logs
- Extracts meaningful error signals
- Uses a local LLM (Ollama + Llama3) for reasoning
- Retrieves similar past incidents using FAISS (RAG)
- Provides a confidence score for RCA reliability
- Includes a Streamlit UI for interactive analysis

## High-Level Architecture
- **UI Layer**: Streamlit interface for log upload and result visualization
- **API Layer**: FastAPI backend handling requests and orchestration
- **AI Layer**: Local LLM for reasoning and RCA generation
- **RAG Layer**: FAISS-based retrieval of historical incidents

## Tech Stack
- Python
- FastAPI
- Streamlit
- Ollama (Llama3)
- LangChain
- FAISS

## How to Run
1. Install Ollama: https://ollama.com  
2. Pull the LLM model:
   ```bash
   ollama pull llama3
3. Install Python dependencies:
pip install -r requirements.txt
4. Start the backend API:
uvicorn app.main:app --reload
5. Start the Streamlit UI:
streamlit run ui/streamlit_app.py

## Why I Built This

Debugging production failures is time-consuming and repetitive.
This project explores how GenAI can assist engineers by automating
initial root cause analysis and reducing mean time to resolution (MTTR).

## Future Improvements:

*Correlate logs across multiple services
*Persist and reuse vector indexes
*Add authentication and role-based access

## Demo Screenshots

### Streamlit UI – Root Cause Analysis Output
![UI Output](screenshots/ui_rca_output.png)

### FastAPI Backend – Log Upload
![API Upload](screenshots/api_upload.png)

### FastAPI Backend – API Response
![API Response](screenshots/api_response.png)
