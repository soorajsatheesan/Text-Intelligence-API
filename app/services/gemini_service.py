import google.generativeai as genai
from app.core.config import GEMINI_API_KEY, GEMINI_MODEL, MODEL_TEMPERATURE
from app.prompts.templates import ANALYZE_PROMPT
from app.schemas.models import AnalysisResponse
from app.utils.parser import extract_json

genai.configure(api_key = GEMINI_API_KEY)

model = genai.GenerativeModel(
    GEMINI_MODEL,
    generation_config={
        "temperature": MODEL_TEMPERATURE,
    },
)

def analyze_text(text: str):
    prompt = ANALYZE_PROMPT.format(input_text = text)

    response = model.generate_content(prompt)

    raw = response.text
    parsed = extract_json(raw)
    return AnalysisResponse(**parsed)
