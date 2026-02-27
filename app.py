# app.py
import streamlit as st
from quiz.data_manager import DataManager
from quiz.quiz import Quiz
from quiz.validation import is_valid_username, is_valid_answer_index

QUESTIONS_FILE = "data/questions.csv"
RESULTS_FILE = "data/results.csv"

# Helper function to initialize quiz
def initialise_quiz():
    questions = DataManager.load_questions_from_csv(QUESTIONS_FILE)
    st.session_state.quiz = Quiz(questions)
    st.session_state.feedback = ""
    st.session_state.answer_submitted = False


# Page setup
st.set_page_config(page_title="IBM Data Platform Quiz", page_icon=":robot_face:")
st.title("IBM Data Platform – New Hire Quiz")

# Initialize session state variables
if "started" not in st.session_state:
    st.session_state.started = False
if "quiz" not in st.session_state:
    st.session_state.quiz = None
if "answer_submitted" not in st.session_state:
    st.session_state.answer_submitted = False
if "feedback" not in st.session_state:
    st.session_state.feedback = ""
if "results_saved" not in st.session_state:
    st.session_state.results_saved = False

# Username input before quiz starts
if not st.session_state.started:
    username = st.text_input("Enter your name to begin:")

    if st.button("Start Quiz"):
        if is_valid_username(username):
            st.session_state.username = username
            initialise_quiz()
            st.session_state.started = True
        else:
            st.error("Please enter a valid name (at least 2 alphanumeric characters).")


# Quiz in progress
else:
    assert st.session_state.quiz is not None, "Quiz should be initialized"
    quiz: Quiz = st.session_state.quiz
    question = quiz.get_current_question()

    st.subheader(f"Question {quiz.current_index + 1} of {len(quiz.questions)}")
    st.write(question.text)

    # Display options as radio buttons
    selected_option = st.radio(
        "Choose an answer:",
        options=list(range(len(question.options))),
        format_func=lambda i: question.options[i],
        key=f"question_{quiz.current_index}",
    )

    # Submit answer
    if st.button("Submit Answer") and not st.session_state.answer_submitted:
        if is_valid_answer_index(selected_option, len(question.options)):
            is_correct = quiz.submit_answer(selected_option)
            st.session_state.feedback = question.get_feedback(is_correct)
            st.session_state.answer_submitted = True
        else:
            st.error("Invalid answer selection.")

    # Show feedback
    if st.session_state.answer_submitted:
        st.info(st.session_state.feedback)

        # Next question button
        if quiz.has_next_question():
            if st.button("Next Question"):
                quiz.next_question()
                st.session_state.answer_submitted = False
        # Quiz completed
        else:
            st.success("🎉 Quiz completed!")
            results = quiz.get_results_summary()
            st.write(
                f"Final Score: {results['score']} / {results['total_questions']}"
            )

            # Save results only once
            if not st.session_state.results_saved:
                DataManager.save_results_to_csv(
                    RESULTS_FILE,
                    st.session_state.username,
                    results["score"],
                    results["total_questions"],
                )
                st.session_state.results_saved = True

    # Optional restart
    if st.button("Restart Quiz"):
        st.session_state.started = False
        st.session_state.quiz = None
        st.session_state.feedback = ""
        st.session_state.answer_submitted = False
        st.session_state.results_saved = False
