import requests
from config import GIGACHAT_API_KEY, GIGACHAT_BASE_URL

class GigaChatClient:
    def __init__(self, system_prompt: str):
        self.system_prompt = system_prompt

    def generate(self, user_message: str, user_state: str | None = None) -> str:
        if not GIGACHAT_API_KEY:
            return "Warning: GIGACHAT_API_KEY not found"

        messages = [
            {"role": "system", "content": self.system_prompt},
        ]

        if user_state:
            messages.append({"role": "system", "content": f"User context: {user_state}"})

        messages.append({"role": "user", "content": user_message})

        headers = {
            "Authorization": f"Bearer {GIGACHAT_API_KEY}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": "GigaChat",
            "messages": messages,
            "temperature": 0.7,
            "top_p": 0.9,
        }

        try:
            resp = requests.post(GIGACHAT_BASE_URL, headers=headers, json=payload, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            return data["choices"][0]["message"]["content"]
        except Exception as e:
            return f"Error: {e}"
