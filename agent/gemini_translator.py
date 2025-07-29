import os
import re
import requests

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def rewrite_with_gemini(text: str) -> str:
    cleaned = re.sub(r'@\w+|https?://\S+', '', text).strip()

    prompt = f"""
Translate the following content into Bahasa Melayu and rewrite it as a casual, friendly Facebook post.
Use natural phrasing with smooth structure and make it feel like it's written by a Malaysian FB user.
Avoid slang or emojis, and don’t include any introduction or notes. Only return the rewritten post content.

'{cleaned}'
"""

    try:
        response = requests.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}",
            headers={"Content-Type": "application/json"},
            json={"contents": [{"parts": [{"text": prompt}]}]}
        )
        return response.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
    except Exception as e:
        print("[Gemini Error]", e)
        return ""

