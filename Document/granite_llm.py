# backend/services/granite_llm.py

import os
import requests
from backend.config import settings

# Constants (replace with IBM Watsonx endpoint structure if known)
GRANITE_API_BASE = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generate"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {settings.GRANITE_API_KEY}"
}


def call_granite(prompt: str, max_tokens: int = 300, temperature: float = 0.7) -> str:
    """
    Send a prompt to IBM Watsonx Granite LLM and return the generated text.
    """
    payload = {
        "model_id": "granite-13b-chat",  # Replace with your actual model name
        "input": prompt,
        "parameters": {
            "decoding_method": "greedy",
            "max_new_tokens": max_tokens,
            "temperature": temperature
        }
    }

    try:
        response = requests.post(GRANITE_API_BASE, headers=HEADERS, json=payload)
        response.raise_for_status()
        return response.json().get("results", [{}])[0].get("generated_text", "⚠️ No response from model.")
    except Exception as e:
        return f"Error calling Granite API: {str(e)}"


def summarize_text(text: str) -> str:
    prompt = f"Summarize the following policy document in plain English:\n\n{text}"
    return call_granite(prompt, max_tokens=250)


def generate_eco_tips(keyword: str) -> list:
    prompt = f"Give me 5 practical eco-friendly tips related to '{keyword}'. List them clearly."
    result = call_granite(prompt, max_tokens=150)
    tips = [tip.strip("-• ") for tip in result.split("\n") if tip.strip()]
    return tips[:5]


def chat_with_assistant(query: str) -> str:
    prompt = f"A citizen asks: '{query}'\nRespond with a helpful, sustainable city-friendly answer."
    return call_granite(prompt, max_tokens=200)
