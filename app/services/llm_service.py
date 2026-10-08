import requests

from app.core.config import OLLAMA_URL, OLLAMA_MODEL

async def get_ai_response(message: str) -> str:

    print("OLLAMA_URL:", OLLAMA_URL)
    print("OLLAMA_MODEL:", OLLAMA_MODEL)

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": message,
            "stream": False
        }
    )

    print("STATUS CODE:", response.status_code)
    print("RESPONSE TEXT:", response.text)

    data = response.json()

    return data["response"]
