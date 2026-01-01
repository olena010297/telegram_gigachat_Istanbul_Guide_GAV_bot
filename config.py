import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GIGACHAT_API_KEY = os.getenv("GIGACHAT_API_KEY")
GIGACHAT_BASE_URL = os.getenv("GIGACHAT_BASE_URL", "https://gigachat.devices.sberbank.ru/api/v1/chat/completions")
