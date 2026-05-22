from fastapi import APIRouter

from app.models.schemas import ChatRequest, ChatResponse
from app.services.llm_service import get_ai_response

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    ai_response = await get_ai_response(request.message)

    return ChatResponse(response=ai_response)
