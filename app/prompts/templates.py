ANALYZE_PROMPT = """
You are a text analysis engine.

Analyze the input text and return STRICT JSON only with this exact schema.
Use exactly these key names with no extra spaces or newlines: summary, keywords, sentiment.

{{
  "summary": "...",
  "keywords": ["k1","k2","k3","k4","k5"],
  "sentiment": "positive | negative | neutral"
}}

Rules:
- Summary max 80 words
- Exactly 5 keywords
- Keywords must be topic terms, not filler words
- Sentiment must be only one of the allowed labels
- No extra text outside JSON

Input text to analyze:

{input_text}
"""
