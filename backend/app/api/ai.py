import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class StrategyRequest(BaseModel):
    prompt: str


@router.post("/ai/generate-strategy")
async def generate_strategy(request: StrategyRequest):
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=503,
            detail="AI assistant not configured. Set OPENROUTER_API_KEY environment variable.",
        )

    from app.services.ai_service import generate_strategy_from_prompt

    try:
        result = await generate_strategy_from_prompt(request.prompt, api_key)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
