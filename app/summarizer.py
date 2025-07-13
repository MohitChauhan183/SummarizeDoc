import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def summarize_text(text):
    if not text.strip():
        return "⚠️ The document appears to be empty or unreadable."

    prompt = (
        "Summarize the following document in no more than 150 words. "
        "Focus on key insights, main ideas, and avoid unnecessary details.\n\n"
        f"{text[:4000]}"
    )

    model = genai.GenerativeModel("gemini-1.5-flash-latest")
    response = model.generate_content(prompt)
    return response.text.strip()
