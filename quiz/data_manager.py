# This file handles loading quiz questions from CSV files and saving quiz results.

import csv
from typing import List
from quiz.question import Question


class DataManager:
    # Manages persistent storage for quiz questions and quiz results.


    @staticmethod
    def load_questions_from_csv(filepath: str) -> List[Question]:
        # Load quiz questions from a CSV file and return a list of Question objects.

        questions: List[Question] = []

        with open(filepath, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            required_fields = {
                "question",
                "option1",
                "option2",
                "option3",
                "option4",
                "correct_index",
                "feedback_correct",
                "feedback_incorrect",
            }

            if not required_fields.issubset(reader.fieldnames or []):
                raise ValueError("CSV file is missing required columns.")

            for row in reader:
                try:
                    options = [
                        row["option1"],
                        row["option2"],
                        row["option3"],
                        row["option4"],
                    ]

                    question = Question(
                        text=row["question"],
                        options=options,
                        correct_index=int(row["correct_index"]),
                        feedback_correct=row["feedback_correct"],
                        feedback_incorrect=row["feedback_incorrect"],
                    )

                    questions.append(question)

                except (KeyError, ValueError) as error:
                    raise ValueError(f"Invalid row in CSV file: {row}") from error

        return questions

    @staticmethod
    def save_results_to_csv(
        filepath: str,
        username: str,
        score: int,
        total_questions: int
    ) -> None:

        # Save quiz results to a CSV file.

        file_exists = False

        try:
            with open(filepath, "r", encoding="utf-8"):
                file_exists = True
        except FileNotFoundError:
            file_exists = False

        with open(filepath, "a", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)

            if not file_exists:
                writer.writerow(["username", "score", "total_questions"])

            writer.writerow([username, score, total_questions])
