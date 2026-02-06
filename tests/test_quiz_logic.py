from quiz.question import Question
from quiz.quiz import Quiz

def create_sample_question(correct_index: int = 1) -> Question:
    return Question(
        text="Sample question",
        options=["A", "B", "C", "D"],
        correct_index=correct_index,
        feedback_correct="Correct",
        feedback_incorrect="Incorrect",
    )


def test_score_increases_on_correct_answer():
    quiz = Quiz([create_sample_question()])
    result = quiz.submit_answer(1)

    assert result is True
    assert quiz.score == 1


def test_score_does_not_increase_on_incorrect_answer():
    quiz = Quiz([create_sample_question()])
    result = quiz.submit_answer(0)

    assert result is False
    assert quiz.score == 0


def test_quiz_progression():
    questions = [create_sample_question(), create_sample_question()]
    quiz = Quiz(questions)

    assert quiz.has_next_question() is True
    quiz.next_question()
    assert quiz.current_index == 1
