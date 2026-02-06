# This doc defines the Question class used to represent a single quiz question.

from typing import List

class Question:
    # Represents a single quiz question with multiple-choice answers.

    def __init__(
        self,
        text: str,
        options: List[str],
        correct_index: int,
        feedback_correct: str,
        feedback_incorrect: str
    ) -> None:
        self.text = text
        self.options = options
        self.correct_index = correct_index
        self.feedback_correct = feedback_correct
        self.feedback_incorrect = feedback_incorrect

    def is_correct(self, answer_index: int) -> bool:
        # Check whether the given answer index is correct.

        return answer_index == self.correct_index

    def get_feedback(self, is_correct: bool) -> str:
        # Return feedback based on whether the answer was correct.

        return self.feedback_correct if is_correct else self.feedback_incorrect

