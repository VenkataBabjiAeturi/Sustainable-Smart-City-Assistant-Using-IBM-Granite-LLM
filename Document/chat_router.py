# backend/routers/chat_router.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from backend.services.llm_service import chat_with_assistant

router = APIRouter(prefix="/chat", tags=["Smart Chat Assistant"])

# Request schema
class ChatQuery(BaseModel):
    query: str

# Endpoint for the chat assistant
@router.post("/")
async def chat(input: ChatQuery):
    try:
        response = chat_with_assistant(input.query)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chat assistant error: {str(e)}")
