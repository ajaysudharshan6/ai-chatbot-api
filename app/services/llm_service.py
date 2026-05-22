import requests

from app.core.config import OLLAMA_URL, OLLAMA_MODEL

async def get_ai_response(message: str) -> str:

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": message,
            "stream": False
        }
    )

    data = response.json()

    return data["response"]
