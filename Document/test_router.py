# tests/test_router.py

import pytest
from httpx import AsyncClient
from fastapi import status

from backend.main import app  # Make sure 'app' is imported from your main FastAPI entry point

# -------------------------------
# Test /chat endpoint
# -------------------------------
@pytest.mark.asyncio
async def test_chat_endpoint():
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.post("/chat/", json={"query": "How can my city save energy?"})
        assert response.status_code == status.HTTP_200_OK
        assert "response" in response.json()
        assert isinstance(response.json()["response"], str)

# -------------------------------
# Test /eco-tips endpoint
# -------------------------------
@pytest.mark.asyncio
async def test_eco_tips_endpoint():
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.post("/eco-tips", json={"keyword": "solar"})
        assert response.status_code == status.HTTP_200_OK
        assert "tips" in response.json()
        assert isinstance(response.json()["tips"], list)

# -------------------------------
# Test /feedback endpoint
# -------------------------------
@pytest.mark.asyncio
async def test_feedback_endpoint():
    payload = {
        "category": "Water",
        "description": "Leaking pipe near 3rd street."
    }
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.post("/feedback", json=payload)
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["status"] == "success"

# -------------------------------
# Test /summarize endpoint
# -------------------------------
@pytest.mark.asyncio
async def test_summarize_endpoint():
    payload = {"text": "This is a long policy about sustainable urban development in smart cities..."}
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.post("/summarize", json=payload)
        assert response.status_code == status.HTTP_200_OK
        assert "summary" in response.json()
