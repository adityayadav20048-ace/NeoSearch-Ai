from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from services.ai_service import generate_stream

router = APIRouter()

@router.post("/ask")
async def ask_ai(data: dict):
    question = data.get("question")

    return StreamingResponse(
        generate_stream(question),
        media_type="text/plain"
    )
