# frontend/page_structures.py

import streamlit as st
import pandas as pd
import requests

from uicomponents import (
    render_header,
    upload_file,
    show_csv_preview,
    render_response_box,
    render_tips,
    chat_input_form
)

API_URL = "http://localhost:8000"  # Modify as needed


# -----------------------------
# 1. 📄 Policy Summarizer
# -----------------------------
def policy_summarizer():
    render_header("City Policy Document Summarizer", "📄")

    file = upload_file("Upload a .txt policy document", ["txt"], key="policy_upload")
    if file:
        text = file.read().decode("utf-8")
        if st.button("Summarize"):
            with st.spinner("Summarizing..."):
                response = requests.post(f"{API_URL}/summarize", json={"text": text})
                if response.status_code == 200:
                    render_response_box("Summary", response.json().get("summary"))
                else:
                    st.error("Failed to get summary from backend.")


# -----------------------------
# 2. 📣 Citizen Feedback
# -----------------------------
def citizen_feedback():
    render_header("Submit Citizen Feedback", "📣")

    category = st.selectbox("Issue Category", ["Water", "Electricity", "Roads", "Sanitation", "Other"])
    description = st.text_area("Describe the issue:")

    if st.button("Submit Feedback"):
        response = requests.post(f"{API_URL}/feedback", json={
            "category": category,
            "description": description
        })
        if response.status_code == 200:
            st.success("✅ Feedback submitted successfully!")
        else:
            st.error("❌ Failed to submit feedback.")


# -----------------------------
# 3. 📊 KPI Forecasting
# -----------------------------
def kpi_forecasting():
    render_header("KPI Forecasting (e.g., Water Usage)", "📊")

    file = upload_file("Upload a KPI CSV file", ["csv"], key="forecast_upload")
    if file:
        show_csv_preview(file)
        file.seek(0)
        if st.button("Generate Forecast"):
            response = requests.post(f"{API_URL}/forecast", files={"file": file})
            if response.status_code == 200:
                data = response.json().get("forecast")
                st.subheader("📈 Forecast Output")
                st.line_chart(pd.DataFrame(data))
            else:
                st.error("Failed to forecast KPI.")


# -----------------------------
# 4. ⚠️ Anomaly Detection
# -----------------------------
def anomaly_detection():
    render_header("KPI Anomaly Detection", "⚠️")

    file = upload_file("Upload a CSV for anomaly check", ["csv"], key="anomaly_upload")
    if file:
        show_csv_preview(file)
        file.seek(0)
        if st.button("Detect Anomalies"):
            response = requests.post(f"{API_URL}/anomaly", files={"file": file})
            if response.status_code == 200:
                anomalies = response.json().get("anomalies")
                st.subheader("🚨 Detected Anomalies")
                st.write(anomalies)
            else:
                st.error("Anomaly detection failed.")


# -----------------------------
# 5. 🌿 Eco Tips Generator
# -----------------------------
def eco_tips_generator():
    render_header("Eco-Friendly Tips Generator", "🌿")

    keyword = st.text_input("Enter a sustainability keyword (e.g., solar, plastic, water):")
    if st.button("Get Eco Tips"):
        response = requests.post(f"{API_URL}/eco-tips", json={"keyword": keyword})
        if response.status_code == 200:
            tips = response.json().get("tips", [])
            render_tips(tips)
        else:
            st.error("Failed to generate eco tips.")


# -----------------------------
# 6. 💬 Smart Chat Assistant
# -----------------------------
def smart_chat_assistant():
    render_header("Smart Chat Assistant", "💬")

    query = chat_input_form()
    if query:
        with st.spinner("Thinking..."):
            response = requests.post(f"{API_URL}/chat", json={"query": query})
            if response.status_code == 200:
                reply = response.json().get("response")
                render_response_box("Assistant Response", reply)
            else:
                st.error("Chat assistant failed to respond.")
