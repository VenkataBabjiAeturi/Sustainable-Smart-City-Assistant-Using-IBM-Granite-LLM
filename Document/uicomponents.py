# frontend/uicomponents.py

import streamlit as st
import pandas as pd

# -----------------------------
# 🔹 Header Section
# -----------------------------
def render_header(title: str, icon: str = "🌆"):
    st.markdown(f"## {icon} {title}")
    st.markdown("---")


# -----------------------------
# 🔹 File Uploader
# -----------------------------
def upload_file(label: str, file_types: list = ["txt", "csv"], key: str = None):
    return st.file_uploader(label, type=file_types, key=key)


# -----------------------------
# 🔹 Show Uploaded Data Preview
# -----------------------------
def show_csv_preview(file, rows: int = 5):
    try:
        df = pd.read_csv(file)
        st.dataframe(df.head(rows))
        return df
    except Exception as e:
        st.error(f"Error reading file: {e}")
        return None


# -----------------------------
# 🔹 Response Box
# -----------------------------
def render_response_box(title: str, content: str):
    st.subheader(title)
    st.success(content)


# -----------------------------
# 🔹 Tips Renderer
# -----------------------------
def render_tips(tips: list):
    st.subheader("💡 Eco-Friendly Tips")
    for tip in tips:
        st.markdown(f"- {tip}")


# -----------------------------
# 🔹 Chat Input Form
# -----------------------------
def chat_input_form():
    with st.form(key="chat_form"):
        query = st.text_input("Type your question:")
        submit = st.form_submit_button("Ask")
        return query if submit else None
