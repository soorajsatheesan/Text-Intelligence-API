import logging

from fastapi import APIRouter, HTTPException
from app.schemas.models import TextRequest, AnalysisResponse
from app.services.gemini_service import analyze_text

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/analyze", response_model=AnalysisResponse)
def analyze(req: TextRequest):
    try:
        result = analyze_text(req.text)
        return result
    except Exception:
        logger.exception("Analysis failed")
        raise HTTPException(status_code=500, detail="Internal server error")