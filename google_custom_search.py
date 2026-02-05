import os
import requests
from dotenv import load_dotenv

load_dotenv()

SEARCH_API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")
SEARCH_CX = os.getenv("GOOGLE_SEARCH_CX")

REALTIME_KEYWORDS = [
    "weather", "price", "today", "now", "current", "latest"
]

def needs_realtime_data(query: str) -> bool:
    return any(k in query.lower() for k in REALTIME_KEYWORDS)


def google_search(query, num_results=3):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": SEARCH_API_KEY,
        "cx": SEARCH_CX,
        "q": query,
        "num": num_results
    }

    try:
        response = requests.get(url, params=params, timeout=8)
        response.raise_for_status()
        data = response.json()

        results = []
        for item in data.get("items", []):
            results.append({
                "title": item.get("title"),
                "snippet": item.get("snippet")
            })

        return results

    except Exception as e:
        print("[WARN] Real-time search unavailable:", e)
        return []   # 👈 graceful fallback
