# frontend/chat_assistant.py

import streamlit as st
import requests

from uicomponents import render_header, render_response_box, chat_input_form

# Replace with your actual backend API URL
API_URL = "http://localhost:8000/chat/"

def main():
    st.set_page_config(page_title="Smart Chat Assistant", layout="centered")
    
    render_header("Smart Chat Assistant", icon="💬")
    st.markdown("Ask sustainability-related questions and get smart responses from the city assistant.")

    query = chat_input_form()
    
    if query:
        with st.spinner("Thinking..."):
            try:
                response = requests.post(API_URL, json={"query": query})
                if response.status_code == 200:
                    reply = response.json().get("response")
                    render_response_box("Assistant Response", reply)
                else:
                    st.error("❌ Failed to get a response from the assistant.")
            except Exception as e:
                st.error(f"⚠️ Error communicating with backend: {str(e)}")


if __name__ == "__main__":
    main()
