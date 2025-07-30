import os
import requests

def query_easypeasy(question: str) -> str:
    url = "https://bots.easy-peasy.ai/bot/e56f7685-30ed-4361-b6c1-8e17495b7faa/api"  # Replace with your actual bot ID
    headers = {
        "content-type": "application/json",
        "x-api-key": os.getenv("EASYPEASY_API_KEY")
    }
    payload = {
        "message": question,
        "history": [],
        "stream": False,
        "include_sources": False
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=20)
        response.raise_for_status()
        return response.json().get("output", "").strip()
    except Exception as e:
        print("[EasyPeasy Error]", e)
        return ""
