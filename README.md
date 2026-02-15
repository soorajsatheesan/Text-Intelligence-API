# Text Intelligence API

A FastAPI-based API that uses Google Gemini to analyze text: summarize content, extract keywords, and classify sentiment. Built for simplicity and reliability.

## Features

- **Summary** — Concise summary of the input text (up to 80 words).
- **Keywords** — Up to 5 topic-focused keywords (no filler words).
- **Sentiment** — Classification as `positive`, `negative`, or `neutral`.

All analysis is returned in a single JSON response.

## Requirements

- **Python 3.10+**
- A [Google AI API key](https://aistudio.google.com/apikey) (for Gemini)

## Quick Start

### 1. Clone and enter the project

```bash
git clone <repository-url>
cd text-intelligence-api
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# or on Windows:
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy the example env file and set your Gemini API key:

```bash
cp .env.example .env
```

Edit `.env` and set at least:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

Optional (defaults shown):

```env
GEMINI_MODEL=gemini-2.5-flash
MODEL_TEMPERATURE=0.2
```

| Variable            | Required | Default              | Description                          |
|---------------------|----------|----------------------|--------------------------------------|
| `GEMINI_API_KEY`    | Yes      | —                    | Google AI (Gemini) API key           |
| `GEMINI_MODEL`      | No       | `gemini-2.5-flash`   | Gemini model name                    |
| `MODEL_TEMPERATURE` | No       | `0.2`                | Model temperature (0–1, lower = more deterministic) |

### 5. Run the API

```bash
uvicorn app.main:app --reload
```

- **API base:** `http://127.0.0.1:8000`
- **Interactive docs (Swagger):** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`

---

## API Reference

### `POST /analyze`

Analyzes the given text and returns a summary, keywords, and sentiment.

#### Request body

| Field  | Type   | Constraints        | Description        |
|--------|--------|--------------------|--------------------|
| `text` | string | 10–10,000 characters | Text to analyze |

Example:

```json
{
  "text": "Your longer piece of text goes here. It should be at least 10 characters and can be up to 10,000 characters for analysis."
}
```

#### Response (200 OK)

| Field       | Type     | Description                    |
|-------------|----------|--------------------------------|
| `summary`   | string   | Short summary (max ~80 words)  |
| `keywords`  | string[] | Up to 5 topic keywords         |
| `sentiment` | string   | `"positive"`, `"negative"`, or `"neutral"` |

Example:

```json
{
  "summary": "The text discusses the benefits of renewable energy and its impact on the environment.",
  "keywords": ["renewable energy", "environment", "sustainability", "climate", "green technology"],
  "sentiment": "positive"
}
```

#### Error responses

| Status | Description |
|--------|-------------|
| `422`  | Validation error (e.g. `text` too short, too long, or missing). |
| `500`  | Internal server error (e.g. API key missing, Gemini error). Response body returns a generic message; details are logged on the server. |

#### cURL example

```bash
curl -X POST "http://127.0.0.1:8000/analyze" \
  -H "Content-Type: application/json" \
  -d '{"text": "Solar and wind power are becoming cheaper and more widespread. Many countries are investing in clean energy to reduce carbon emissions and combat climate change."}'
```

---

## Project structure

```
text-intelligence-api/
├── app/
│   ├── api/
│   │   └── routes.py       # API route: POST /analyze
│   ├── core/
│   │   └── config.py       # Environment and config (API key, model, temperature)
│   ├── prompts/
│   │   └── templates.py    # Gemini prompt template
│   ├── schemas/
│   │   └── models.py       # Pydantic models (TextRequest, AnalysisResponse)
│   ├── services/
│   │   └── gemini_service.py  # Gemini client and analyze_text()
│   ├── utils/
│   │   └── parser.py       # JSON extraction and key normalization from model output
│   └── main.py             # FastAPI app entry point
├── .env.example
├── requirements.txt
└── README.md
```

- **routes** — HTTP layer; calls the service and handles errors.
- **config** — Loads `.env` and validates `GEMINI_API_KEY`.
- **gemini_service** — Builds the prompt, calls Gemini, parses and normalizes the response, returns an `AnalysisResponse`.
- **parser** — Finds JSON in the model output, normalizes keys (e.g. handles stray newlines), and returns a dict suitable for Pydantic.

---

## Development

- Run with auto-reload: `uvicorn app.main:app --reload`
- Dependencies include `pytest` and `httpx` for writing tests; add tests under a `tests/` directory and run with `pytest`.

---

## License

MIT
