# This file contains pure functions for validating user input.

def is_valid_username(username: str) -> bool:
    # Validate a username.

    if not username:
        return False

    if len(username.strip()) < 2:
        return False

    return username.replace(" ", "").isalnum()

def is_valid_answer_index(index: int, num_options: int) -> bool:
    # Validate an answer index.

    if not isinstance(index, int):
        return False

    return 0 <= index < num_options
