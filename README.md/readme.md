# Smart Assistant for Research Summarization

An AI-powered research assistant that reads user-uploaded documents (PDF or TXT), provides contextual summaries, answers free-form questions with memory, and challenges users with logic-based questions, all grounded in the document content.

---

## 🚀 Features

- **Document Upload**: Upload PDF or TXT files.
- **Auto Summary**: Generate concise summaries (≤150 words) instantly.
- **Ask Anything**: Free-form Q&A with memory — follow-up questions remember prior context.
- **Challenge Me**: Generate 3 logic-based questions from the document, accept user answers, and provide detailed evaluation with supporting document snippets.
- **Answer Justification**: All answers are justified with references to the document to minimize hallucinations.

---

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.8 or later installed
- A Google Gemini API key (set up your Google Cloud account to get the key)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/smart-assistant-genai.git
   cd smart-assistant-genai
