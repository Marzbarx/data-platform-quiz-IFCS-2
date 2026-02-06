from quiz.validation import is_valid_username, is_valid_answer_index


def test_valid_username():
    assert is_valid_username("Alice") is True
    assert is_valid_username("A1") is True


def test_invalid_username():
    assert is_valid_username("") is False
    assert is_valid_username(" ") is False
    assert is_valid_username("A") is False


def test_valid_answer_index():
    assert is_valid_answer_index(0, 4) is True
    assert is_valid_answer_index(3, 4) is True


def test_invalid_answer_index():
    assert is_valid_answer_index(-1, 4) is False
    assert is_valid_answer_index(4, 4) is False
