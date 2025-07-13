import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model_name = "gemini-1.5-flash-latest"
model = genai.GenerativeModel(model_name)

response = model.generate_content("Explain quantum computing in one paragraph.")
print(response.text)
