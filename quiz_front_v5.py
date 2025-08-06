import streamlit as st
import random
from questions import question_bank

def reset_quiz():
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.incorrect_answers = []
    st.session_state.answered = {}
    st.session_state.shuffled_questions = random.sample(question_bank, len(question_bank))
    for key in list(st.session_state.keys()):
        if key.startswith("question_") or key.startswith("answered_"):
            del st.session_state[key]

def run_quiz():
    if "current_question" not in st.session_state:
        reset_quiz()

    total_questions = len(st.session_state.shuffled_questions)
    current_index = st.session_state.current_question
    st.progress(current_index / total_questions)

    if current_index < total_questions:
        question_data = st.session_state.shuffled_questions[current_index]
        question_text = question_data["question"]
        options = question_data["options"]
        correct_answer = options[question_data["answer"][0] - 1]

        st.title("Quiz on Distributed Systems and Big Data")
        st.subheader(f"Question {current_index + 1} of {total_questions}")
        st.write(question_text)

        # ✅ Show image if available
        if "image" in question_data:
            st.image(f"pic/{question_data['image']}", use_container_width=False)

        answered_key = f"answered_{current_index}"
        widget_key = f"question_{current_index}"

        # Use a radio button with placeholder
        all_options = ["Select an option"] + options
        user_answer = st.radio("Choose an answer:", all_options, key=widget_key)
        answered = st.session_state.get(answered_key, False)

        if user_answer != "Select an option" and not answered:
            st.session_state[answered_key] = True
            if user_answer == correct_answer:
                st.session_state.score += 1
            else:
                st.session_state.incorrect_answers.append((question_text, [correct_answer]))
            st.session_state.current_question += 1
            st.rerun()

    else:
        st.balloons()
        st.success(f"🎉 Quiz Completed! Your final score is {st.session_state.score}/{total_questions}")
        if st.session_state.incorrect_answers:
            st.subheader("Review Your Incorrect Answers:")
            for q_text, correct_opts in st.session_state.incorrect_answers:
                st.write(f"**Question:** {q_text}")
                st.write(f"**Correct Answer:** {', '.join(correct_opts)}")
        if st.button("Restart Quiz"):
            reset_quiz()
            st.rerun()

if __name__ == "__main__":
    run_quiz()
