import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash-latest")

# --- Ask Anything with Memory Handling ---
def ask_question(document_text, user_question, conversation_history=None):
    history_prompt = ""
    if conversation_history:
        recent_history = conversation_history[-5:]  # Limit to last 5 turns
        for i, turn in enumerate(recent_history):
            history_prompt += f"Q{i+1}: {turn['question']}\nA{i+1}: {turn['answer']}\n"

    prompt = f"""You are an assistant that answers questions based on documents and maintains context for follow-up questions.

Document:
\"\"\"
{document_text[:4000]}
\"\"\"

Conversation so far:
{history_prompt}

Now answer the following question using the document and prior conversation:

Q: {user_question}

Provide a direct answer and a short justification from the document.
"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error generating answer: {e}"


# --- Challenge Me: Generate Questions ---
def generate_challenge_questions(document_text, num_questions=3):
    prompt = f"""
You are an AI assistant. Based on the following document text, generate {num_questions} challenging comprehension questions that require reasoning and deep understanding. Make sure the questions are answerable based on the text.

Document Text:
\"\"\"
{document_text[:4000]}
\"\"\"

Questions:
1."""
    try:
        response = model.generate_content(prompt)
        questions_text = response.text.strip()

        questions = []
        for i in range(1, num_questions + 1):
            start_idx = questions_text.find(f"{i}.")
            if start_idx == -1:
                continue
            end_idx = questions_text.find(f"{i+1}.") if i < num_questions else len(questions_text)
            question = questions_text[start_idx + 2:end_idx].strip().replace('\n', ' ')
            if question:
                questions.append(question)

        return questions

    except Exception as e:
        return [f"❌ Error generating questions: {e}"]


# --- Challenge Me: Evaluate User's Answer ---
def evaluate_challenge_answer(question, user_answer, document_text):
    prompt = f"""
You are an AI assistant. Given the document text, question, and user's answer below, evaluate if the answer is correct and provide detailed feedback. Your feedback must be grounded in the document, citing relevant paragraphs or sections.

Also, provide the exact snippet from the document that supports your evaluation.

Format your response as:

Evaluation: <your detailed feedback>
Supporting Snippet: <exact text from the document>

Document Text:
\"\"\"
{document_text[:4000]}
\"\"\"

Question:
{question}

User's Answer:
{user_answer}

Response:
"""

    try:
        response = model.generate_content(prompt)
        text = response.text.strip()

        if "Supporting Snippet:" in text:
            eval_text, snippet = text.split("Supporting Snippet:", 1)
            return f"{eval_text.strip()}\n\n**Supporting Snippet:**\n{snippet.strip()}"
        else:
            return text

    except Exception as e:
        return f"❌ Error evaluating answer: {e}"
