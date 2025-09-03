import pytest
from task_2 import assign_grade

def test_assign_grade_valid_scores():
    assert assign_grade(95) == "A"
    assert assign_grade(90) == "A"
    assert assign_grade(89) == "B"
    assert assign_grade(80) == "B"
    assert assign_grade(79) == "C"
    assert assign_grade(70) == "C"
    assert assign_grade(69) == "D"
    assert assign_grade(60) == "D"
    assert assign_grade(59) == "F"
    assert assign_grade(0) == "F"

def test_assign_grade_invalid_type():
    assert assign_grade("abc") == "Invalid input: Score must be a number."
    assert assign_grade(None) == "Invalid input: Score must be a number."
    assert assign_grade([90]) == "Invalid input: Score must be a number."

def test_assign_grade_out_of_range():
    assert assign_grade(-1) == "Invalid input: Score must be between 0 and 100."
    assert assign_grade(101) == "Invalid input: Score must be between 0 and 100."
    assert assign_grade(100.1) == "Invalid input: Score must be between 0 and 100."