import pytest
from task_3 import sentence_palindrome

@pytest.mark.parametrize("sentence,expected", [
    ("A man, a plan, a canal: Panama", True),
    ("No lemon, no melon", True),
    ("Was it a car or a cat I saw?", True),
    ("Hello, World!", False),
    ("", True),  # Empty string is a palindrome
    ("12321", True),
    ("12345", False),
    ("Able was I, ere I saw Elba", True),
    ("Step on no pets", True),
    ("Not a palindrome", False),
])
def test_sentence_palindrome(sentence, expected):
    assert sentence_palindrome(sentence) == expected