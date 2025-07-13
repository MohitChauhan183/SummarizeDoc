import streamlit as st
from document_parser import extract_text
from summarizer import summarize_text
from qa_engine import (
    ask_question,
    generate_challenge_questions,
    evaluate_challenge_answer,
)

st.set_page_config(page_title="Smart Research Assistant")

st.title("📄 Smart Assistant for Research Summarization")

uploaded_file = st.file_uploader("Upload a PDF or TXT document", type=["pdf", "txt"])

if uploaded_file:
    file_text = extract_text(uploaded_file)
    st.session_state["document_text"] = file_text

    # Reset previous sessions when a new file is uploaded
    st.session_state.pop("conversation_history", None)
    st.session_state.pop("challenge_questions", None)
    st.session_state.pop("user_answers", None)
    st.session_state.pop("evaluations", None)

    st.subheader("📌 Auto Summary")
    summary = summarize_text(file_text)
    st.write(summary)

    mode = st.radio("Choose interaction mode:", ["Ask Anything", "Challenge Me"])

    if mode == "Ask Anything":
        st.subheader("💬 Ask Anything")

        if "conversation_history" not in st.session_state:
            st.session_state.conversation_history = []

        # Show previous Q&A
        for i, turn in enumerate(st.session_state.conversation_history):
            st.markdown(f"**Q{i + 1}:** {turn['question']}")
            st.markdown(f"**A{i + 1}:** {turn['answer']}")
            if turn.get("justification"):
                st.markdown(f"*Justification:* {turn['justification']}")

        user_q = st.text_input("Enter your question:")

        if user_q:
            response = ask_question(
                file_text,
                user_q,
                conversation_history=st.session_state.conversation_history,
            )

            st.session_state.conversation_history.append({
                "question": user_q,
                "answer": response,
                "justification": "",  # Can be extended to extract if needed
            })

            st.write("**Answer:**", response)

    elif mode == "Challenge Me":
        st.subheader("🧠 Challenge Me")

        if "challenge_questions" not in st.session_state:
            with st.spinner("Generating challenge questions..."):
                questions = generate_challenge_questions(file_text)
                st.session_state.challenge_questions = questions
                st.session_state.user_answers = [""] * len(questions)
                st.session_state.evaluations = [None] * len(questions)

        questions = st.session_state.challenge_questions
        user_answers = st.session_state.user_answers
        evaluations = st.session_state.evaluations

        for i, question in enumerate(questions):
            st.markdown(f"**Q{i + 1}:** {question}")
            user_answers[i] = st.text_area(
                f"Your answer for Q{i + 1}:",
                value=user_answers[i],
                key=f"answer_{i}"
            )

        if st.button("Submit Answers for Evaluation"):
            if all(ans.strip() for ans in user_answers):
                with st.spinner("Evaluating your answers..."):
                    for i, (question, answer) in enumerate(zip(questions, user_answers)):
                        evaluations[i] = evaluate_challenge_answer(question, answer, file_text)
                    st.session_state.evaluations = evaluations
            else:
                st.warning("⚠️ Please answer all questions before submitting.")

        for i, evaluation in enumerate(evaluations):
            if evaluation:
                st.markdown(f"**Feedback for Q{i + 1}:**")
                st.write(evaluation)
