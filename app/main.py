from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title = "Text Intelligence API",
    description="Summarize text, extract keywords, classify sentiment",
    version = "1.0.0",
)

app.include_router(router)