# Text Intelligence API

A FastAPI-based API for text intelligence features.

## Requirements

- Python 3.10+

## Setup

1. Clone the repository and enter the project directory:

   ```bash
   cd text-intelligence-api
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   # or: .venv\Scripts\activate   # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. (Optional) Copy `.env.example` to `.env` and set any environment variables.

## Running the API

Start the development server:

```bash
uvicorn main:app --reload
```

Replace `main:app` with your actual app module and instance (e.g. `app.main:app`) if different.

- API: `http://127.0.0.1:8000`
- Interactive docs: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## License

MIT
