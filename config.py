import os
import requests
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# API KEYS
GEMINI_API_KEY = os.getenv("AIzaSyDdB4fEyiFCeHlQ2lp_GKxP1sOiKvZf8cI")
SEARCH_API_KEY = os.getenv("AIzaSyDCi0WUdLr6BzmGGdGN_5LBHP_yLOIB6rg")
SEARCH_CX = os.getenv("8302a9685faf64e82")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.0-pro")
