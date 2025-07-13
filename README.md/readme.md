📄 SummarizeDoc – AI-Powered Research Summarization Assistant
SummarizeDoc is an intelligent web application that helps users quickly understand and interact with lengthy documents such as research papers, technical manuals, or legal files. Leveraging Google Gemini AI, it provides concise summaries, context-aware Q&A, and logic-based challenge questions — all with document-grounded justifications.

🚀 Features
📑 Auto Summary: Generates a concise summary of uploaded PDFs or TXT files (≤150 words)

💬 Ask Anything: Free-form question answering with memory to handle follow-ups

🧠 Challenge Me: Generates reasoning-based questions, evaluates user answers, and provides detailed feedback with exact supporting text from the document

📂 Multi-format Support: Upload PDF or plain text documents

🔒 Local, Secure: Runs locally via a clean Streamlit interface, keeping user data private


🛠️ Tech Stack
Frontend: Streamlit (Python)

Backend: Python modules for document parsing, summarization, Q&A, and challenge logic

AI Integration: Google Gemini API

Document Parsing: PyMuPDF for PDFs, UTF-8 decoding for text files

Environment: Virtual environment with dependencies managed via requirements.txt

🧠 AI Integration
SummarizeDoc uses Google Gemini’s generative language models to:

Understand and summarize large text documents

Answer questions contextually with memory of previous Q&A turns

Generate challenging comprehension questions and evaluate user responses

Justify every answer by citing relevant excerpts from the source document

🔧 How to Run Locally

# Clone the repo
git clone https://github.com/MohitChauhan183/SummarizeDoc.git
cd SummarizeDoc

# Create and activate virtual environment
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/macOS
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file and add your Gemini API key
# GEMINI_API_KEY=your_google_gemini_api_key_here

# Run the Streamlit app
streamlit run app/main.py

