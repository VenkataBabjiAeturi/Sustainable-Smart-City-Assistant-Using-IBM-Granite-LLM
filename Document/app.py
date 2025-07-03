# frontend/app.py

import streamlit as st
import requests
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Sustainable Smart City Assistant",
    layout="wide",
    initial_sidebar_state="expanded"
)

# API base URL
API_URL = "http://localhost:8000"

# Sidebar menu
st.sidebar.title("🧭 Navigation")
menu = st.sidebar.radio(
    "Choose a feature:",
    ("🏙️ Policy Summarizer", 
     "📣 Citizen Feedback", 
     "📊 KPI Forecasting", 
     "⚠️ Anomaly Detection", 
     "🌿 Eco Tips Generator", 
     "💬 Smart Chat Assistant")
)

st.title("🌆 Sustainable Smart City Assistant")

# -------------------------
# 1. Policy Summarizer
# -------------------------
if menu == "🏙️ Policy Summarizer":
    st.header("📄 City Policy Document Summarizer")

    uploaded_file = st.file_uploader("Upload a policy document (.txt)", type=["txt"])
    if uploaded_file is not None:
        content = uploaded_file.read().decode("utf-8")
        if st.button("Summarize"):
            with st.spinner("Summarizing..."):
                response = requests.post(f"{API_URL}/summarize", json={"text": content})
                if response.status_code == 200:
                    st.subheader("📝 Summary")
                    st.write(response.json().get("summary"))
                else:
                    st.error("Failed to summarize the document.")

# -------------------------
# 2. Citizen Feedback
# -------------------------
elif menu == "📣 Citizen Feedback":
    st.header("🗣️ Submit Citizen Feedback")

    category = st.selectbox("Issue Category", ["Water", "Electricity", "Roads", "Sanitation", "Other"])
    description = st.text_area("Describe the issue:")
    
    if st.button("Submit Feedback"):
        payload = {"category": category, "description": description}
        response = requests.post(f"{API_URL}/feedback", json=payload)
        if response.status_code == 200:
            st.success("✅ Feedback submitted successfully!")
        else:
            st.error("❌ Failed to submit feedback.")

# -------------------------
# 3. KPI Forecasting
# -------------------------
elif menu == "📊 KPI Forecasting":
    st.header("📈 Upload KPI Data for Forecasting")

    uploaded_csv = st.file_uploader("Upload CSV file (e.g., water usage)", type=["csv"])
    if uploaded_csv is not None:
        df = pd.read_csv(uploaded_csv)
        st.write("📋 Uploaded Data", df.head())
        if st.button("Generate Forecast"):
            response = requests.post(
                f"{API_URL}/forecast",
                files={"file": uploaded_csv}
            )
            if response.status_code == 200:
                forecast_data = response.json().get("forecast")
                st.subheader("📉 Forecast Results")
                st.line_chart(pd.DataFrame(forecast_data))
            else:
                st.error("Forecasting failed.")

# -------------------------
# 4. Anomaly Detection
# -------------------------
elif menu == "⚠️ Anomaly Detection":
    st.header("🚨 Upload KPI for Anomaly Detection")

    uploaded_csv = st.file_uploader("Upload KPI CSV", type=["csv"], key="anomaly_csv")
    if uploaded_csv is not None:
        df = pd.read_csv(uploaded_csv)
        st.write("📋 Uploaded Data", df.head())
        if st.button("Detect Anomalies"):
            response = requests.post(
                f"{API_URL}/anomaly",
                files={"file": uploaded_csv}
            )
            if response.status_code == 200:
                anomalies = response.json().get("anomalies")
                st.subheader("⚠️ Anomalies Found")
                st.write(anomalies)
            else:
                st.error("Anomaly detection failed.")

# -------------------------
# 5. Eco Tips Generator
# -------------------------
elif menu == "🌿 Eco Tips Generator":
    st.header("🌍 Get Eco-Friendly Tips")

    keyword = st.text_input("Enter a sustainability keyword (e.g., 'solar', 'plastic'):")
    if st.button("Generate Tips"):
        response = requests.post(f"{API_URL}/eco-tips", json={"keyword": keyword})
        if response.status_code == 200:
            tips = response.json().get("tips")
            st.subheader("💡 Eco Tips")
            for tip in tips:
                st.markdown(f"- {tip}")
        else:
            st.error("Could not generate tips.")

# -------------------------
# 6. Smart Chat Assistant
# -------------------------
elif menu == "💬 Smart Chat Assistant":
    st.header("💬 Ask the City Assistant")

    user_question = st.text_input("Type your question about sustainability or smart cities:")
    if st.button("Ask"):
        response = requests.post(f"{API_URL}/chat", json={"query": user_question})
        if response.status_code == 200:
            answer = response.json().get("response")
            st.subheader("🤖 Assistant's Answer")
            st.write(answer)
        else:
            st.error("Failed to get response from assistant.")
