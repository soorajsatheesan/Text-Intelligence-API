import os
from dotenv import load_dotenv

#Code to access .env varaibles
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
MODEL_TEMPERATURE = float(os.getenv("MODEL_TEMPERATURE","0.2"))

if not GEMINI_API_KEY:
    raise ValueError("Missing GEMINI_API_KEY in environment")