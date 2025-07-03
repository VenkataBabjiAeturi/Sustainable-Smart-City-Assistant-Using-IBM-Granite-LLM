# backend/services/granite_llmservice.py

import requests
from backend.config import settings

# IBM Watsonx Granite API base endpoint (replace with actual if different)
GRANITE_API_URL = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generate"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {settings.GRANITE_API_KEY}"
}


def call_granite_llm(prompt: str, max_tokens: int = 300, temperature: float = 0.7) -> str:
    """
    Sends a prompt to IBM Granite LLM and returns the generated response.
    """
    payload = {
        "model_id": "granite-13b-chat",  # Replace with correct model ID if needed
        "input": prompt,
        "parameters": {
            "decoding_method": "greedy",
            "max_new_tokens": max_tokens,
            "temperature": temperature
        }
    }

    try:
        response = requests.post(GRANITE_API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        result = response.json()
        return result.get("results", [{}])[0].get("generated_text", "⚠️ No response from LLM.")
    except Exception as e:
        return f"❌ Error calling Granite API: {str(e)}"


def summarize_text(text: str) -> str:
    """
    Uses Granite LLM to summarize a policy document.
    """
    prompt = f"Summarize the following city policy document in plain, concise language for citizens:\n\n{text}"
    return call_granite_llm(prompt, max_tokens=250)


def generate_eco_tips(keyword: str) -> list:
    """
    Generates 5 eco-friendly tips based on a given keyword (e.g., 'solar').
    """
    prompt = f"Provide 5 clear, practical eco-friendly tips related to '{keyword}':"
    output = call_granite_llm(prompt, max_tokens=150)
    tips = [tip.strip("-• \n") for tip in output.split("\n") if tip.strip()]
    return tips[:5]


def chat_with_assistant(query: str) -> str:
    """
    Handles a user query with a smart sustainability-aware response.
    """
    prompt = (
        f"You are a helpful assistant for a sustainable smart city. "
        f"Answer the citizen's question in an informative and friendly way.\n\n"
        f"Citizen: {query}\nAssistant:"
    )
    return call_granite_llm(prompt, max_tokens=200)
