# Defines the Quiz class which manages quiz state, progression, and scoring.

from typing import List, Dict
from quiz.question import Question

class Quiz:
    # Manages quiz progression, scoring, and user responses.

    def __init__(self, questions: List[Question]) -> None:
        # Initialise the quiz with a list of questions.

        self.questions = questions
        self.current_index = 0
        self.score = 0
        self.user_answers: Dict[int, int] = {}

    def get_current_question(self) -> Question:
        # Return the current question.

        return self.questions[self.current_index]

    def submit_answer(self, answer_index: int) -> bool:
        # Submit an answer for the current question and update score.

        question = self.get_current_question()
        is_correct = question.is_correct(answer_index)

        self.user_answers[self.current_index] = answer_index

        if is_correct:
            self.score += 1

        return is_correct

    def next_question(self) -> None:
       
        # Move to the next question in the quiz.
    
        if self.has_next_question():
            self.current_index += 1

    def has_next_question(self) -> bool:
        # Check if there are more questions remaining.

        
        return self.current_index < len(self.questions) - 1

    def get_results_summary(self) -> dict:
        # Return a summary of the quiz results.

        return {
            "score": self.score,
            "total_questions": len(self.questions),
        }
