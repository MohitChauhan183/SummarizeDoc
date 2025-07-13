import google.generativeai as genai
import streamlit as st


genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

def summarize_text(text):
    if not text.strip():
        return "⚠️ The document appears to be empty or unreadable."

    prompt = (
        "Summarize the following document in no more than 150 words. "
        "Focus on key insights, main ideas, and avoid unnecessary details.\n\n"
        f"{text[:4000]}"
    )

    model = genai.GenerativeModel("gemini-2.5-flash-lite-preview-06-17")
    response = model.generate_content(prompt)
    return response.text.strip()
