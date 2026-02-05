import os
from dotenv import load_dotenv
import google.generativeai as genai

from memory import ConversationMemory
from google_custom_search import google_search, needs_realtime_data

# Load env
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ✅ Correct model name
model = genai.GenerativeModel("models/gemini-flash-latest")

def generate_response(user_query: str, memory: ConversationMemory) -> str:
    realtime_context = ""

    if needs_realtime_data(user_query):
        results = google_search(user_query)
        realtime_context = "\n".join(
            f"- {r['title']}: {r['snippet']}" for r in results
        )

    prompt = f"""
You are a helpful AI assistant.
Use real-time information ONLY if provided.

Real-time information:
{realtime_context}

User question:
{user_query}
"""

    chat = model.start_chat(history=memory.get())
    response = chat.send_message(prompt)

    answer = response.text

    memory.add_user(user_query)
    memory.add_model(answer)

    return answer
