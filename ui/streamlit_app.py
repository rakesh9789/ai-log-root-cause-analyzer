import streamlit as st
import requests

API_ENDPOINT = "http://localhost:8000/analyze-log"

st.set_page_config(page_title="AI Log RCA", layout="wide")

st.title("AI Log Root Cause Analyzer")
st.write(
    "This tool analyzes application logs and generates "
    "root cause analysis using a local LLM and historical incidents."
)

uploaded_log = st.file_uploader(
    "Upload application log file",
    type=["log", "txt"]
)

if uploaded_log:
    log_content = uploaded_log.read().decode("utf-8")

    st.subheader("Log Preview")
    st.code(log_content, language="text")

    if st.button("Run Root Cause Analysis"):
        with st.spinner("Running AI analysis..."):
            response = requests.post(
                API_ENDPOINT,
                files={"file": (uploaded_log.name, log_content)}
            )

        if response.status_code == 200:
            result = response.json()

            left, right = st.columns(2)

            with left:
                st.subheader("Detected Error Signals")
                for err in result["error_signals"]:
                    st.error(err)

                st.subheader("Confidence Score")

                st.metric(
                    label="RCA Confidence",
                    value=f"{int(result['confidence_score'] * 100)}%",
                    delta=None
                )

                st.progress(result["confidence_score"])


            with right:
                st.subheader("RCA Report")
                st.write(result["rca_report"])

                st.subheader("Related Historical Incidents")
                for incident in result["related_incidents"]:
                    st.info(incident)
        else:
            st.error("Backend service is not running.")
