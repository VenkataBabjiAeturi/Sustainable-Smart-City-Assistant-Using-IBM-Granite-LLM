# frontend/kpi_file_forecaster.py

import streamlit as st
import pandas as pd
import requests

from uicomponents import render_header, upload_file, show_csv_preview

# Backend API URL (adjust as needed)
API_ENDPOINT = "http://localhost:8000/forecast"

def main():
    st.set_page_config(page_title="KPI Forecasting", layout="centered")

    render_header("📊 KPI Forecasting Assistant", "📊")
    st.markdown("Upload a CSV file with historical KPI data (e.g., water or energy usage) to generate forecasts.")

    file = upload_file("Upload KPI CSV file", ["csv"], key="kpi_upload")

    if file:
        df = show_csv_preview(file)
        file.seek(0)  # Reset file pointer after preview

        if st.button("🔮 Generate Forecast"):
            with st.spinner("Forecasting..."):
                try:
                    response = requests.post(API_ENDPOINT, files={"file": file})
                    if response.status_code == 200:
                        forecasted_data = response.json().get("forecast")

                        if forecasted_data:
                            st.success("✅ Forecast generated successfully!")
                            forecast_df = pd.DataFrame(forecasted_data)
                            st.line_chart(forecast_df)
                        else:
                            st.warning("No forecast data returned.")
                    else:
                        st.error(f"❌ API Error: {response.status_code}")
                except Exception as e:
                    st.error(f"⚠️ Error connecting to backend: {e}")

if __name__ == "__main__":
    main()
