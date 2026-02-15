from pydantic import BaseModel, Field
from typing import List

class TextRequest(BaseModel):
    text: str = Field(min_lenth=10, max_length=10000)

class AnalysisResponse(BaseModel):
    summary: str
    keywords: List[str]
    sentiment: str