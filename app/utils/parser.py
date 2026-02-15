import json
import re

# Expected keys for analysis response (after normalizing)
EXPECTED_KEYS = {"summary", "keywords", "sentiment"}


def _normalize_keys(data: dict) -> dict:
    """Strip whitespace/newlines from keys and keep only expected keys."""
    result = {}
    for key, value in data.items():
        clean_key = key.strip().strip('"')
        if clean_key in EXPECTED_KEYS:
            result[clean_key] = value
    return result


def extract_json(text: str) -> dict:
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError("No JSON found in model response")

    parsed = json.loads(match.group(0))
    if not isinstance(parsed, dict):
        raise ValueError("Parsed JSON is not an object")

    return _normalize_keys(parsed)
