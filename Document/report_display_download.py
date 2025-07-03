# frontend/report_display_download.py

import streamlit as st

from io import BytesIO

def render_report_section(report_title: str, report_content: str):
    """
    Displays the AI-generated report with options to download as a text file.
    """
    st.header(report_title)
    st.markdown(report_content)

    # Prepare download button
    report_bytes = report_content.encode("utf-8")
    buffer = BytesIO(report_bytes)

    st.download_button(
        label="📥 Download Report as TXT",
        data=buffer,
        file_name="city_sustainability_report.txt",
        mime="text/plain"
    )


def main():
    st.set_page_config(page_title="Report Viewer & Download", layout="centered")

    st.title("📋 Sustainability Report Viewer")

    report_content = st.text_area(
        "Paste or generate your sustainability report here:",
        height=300,
        help="You can paste AI-generated summaries or KPI reports to view and download."
    )

    if report_content.strip():
        render_report_section("Generated Report", report_content)
    else:
        st.info("Paste a report above or generate one from other modules to view here.")


if __name__ == "__main__":
    main()
