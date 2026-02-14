from fastapi import APIRouter, Request, HTTPException
from app.services import generation_service

router = APIRouter()

@router.post("/generate")
async def generate_mql(request: Request):
    try:
        data = await request.json()
        result = generation_service.generate(data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate/preview")
async def preview_mql(request: Request):
    try:
        data = await request.json()
        result = generation_service.generate(data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
