import os
import requests

FB_PAGE_ID = os.getenv("FB_PAGE_ID")
FB_LONG_TOKEN = os.getenv("LONG_LIVED_USER_TOKEN")

def get_fb_token():
    try:
        res = requests.get(
            f"https://graph.facebook.com/v19.0/me/accounts?access_token={FB_LONG_TOKEN}"
        )
        return res.json()["data"][0]["access_token"]
    except Exception as e:
        print("[FB Token Error]", e)
        return None

def post_to_facebook(message: str) -> bool:
    token = get_fb_token()
    if not token:
        return False

    try:
        r = requests.post(
            f"https://graph.facebook.com/{FB_PAGE_ID}/feed",
            data={"message": message, "access_token": token}
        )
        if r.status_code == 200:
            print("[✅ Posted to Facebook]")
            return True
        else:
            print("[❌ FB Post Error]", r.text)
            return False
    except Exception as e:
        print("[FB Post Exception]", e)
        return False

