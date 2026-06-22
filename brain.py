"""
Requires GEMINI_API_KEY to be set as an environment variable. Get a free
key at https://aistudio.google.com/app/apikey
"""

import os
import warnings

warnings.filterwarnings("ignore", category=FutureWarning, module="google.generativeai")
import google.generativeai as genai

API_KEY = os.getenv("GEMINI_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)


def ask_llm(prompt):
    if not API_KEY:
        return "No Gemini API key found. Set the GEMINI_API_KEY environment variable to enable this."

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(
            f"You are Jarvis, a concise AI assistant. Respond briefly to: {prompt}"
        )
        return response.text.strip()

    except Exception as e:
        return f"Brain error: {e}"
