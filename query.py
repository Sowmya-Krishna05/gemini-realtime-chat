REALTIME_KEYWORDS = [
    "current", "today", "price", "weather",
    "latest", "now", "live"
]

def needs_realtime_data(query):
    query_lower = query.lower()
    return any(word in query_lower for word in REALTIME_KEYWORDS)
