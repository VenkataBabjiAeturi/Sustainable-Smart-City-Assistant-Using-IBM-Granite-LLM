# frontend/anomaly_filechecker.py

import streamlit as st
import pandas as pd
import requests

from uicomponents import render_header, upload_file, show_csv_preview

# Backend endpoint for anomaly detection
API_ENDPOINT = "http://localhost:8000/anomaly"

def main():
    st.set_page_config(page_title="KPI Anomaly Detector", layout="centered")

    render_header("⚠️ KPI Anomaly Detection", "⚠️")
    st.markdown(
        "Upload a KPI CSV file (e.g., monthly energy or water usage by city sectors). "
        "The assistant will detect unusual spikes or drops."
    )

    file = upload_file("Upload KPI CSV", ["csv"], key="anomaly_upload")

    if file:
        df = show_csv_preview(file)
        file.seek(0)

        if st.button("🔍 Detect Anomalies"):
            with st.spinner("Analyzing for anomalies..."):
                try:
                    response = requests.post(API_ENDPOINT, files={"file": file})
                    if response.status_code == 200:
                        anomalies = response.json().get("anomalies", [])

                        if anomalies:
                            st.subheader("🚨 Detected Anomalies")
                            st.write(anomalies)
                        else:
                            st.success("✅ No significant anomalies found.")
                    else:
                        st.error(f"❌ Error: {response.status_code}")
                except Exception as e:
                    st.error(f"⚠️ Connection Error: {e}")

if __name__ == "__main__":
    main()
