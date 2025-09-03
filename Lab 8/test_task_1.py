import pytest
from task_1 import is_valid_email

@pytest.mark.parametrize("email", [
    "user@example.com",
    "john.doe@domain.co.uk",
    "a-b_c.d@sub.domain.com",
])
def test_valid_emails(email):
    assert is_valid_email(email) is True

@pytest.mark.parametrize("email", [
    "userexample.com",         # missing @
    "user@examplecom",         # missing .
    "user@@example.com",       # multiple @
    "@user@example.com",       # starts with special char
    "user@example.com.",       # ends with special char
    "user@.example.com",       # starts with special char after @
    "user@example.com-",       # ends with special char
    ".user@example.com",       # starts with special char
    "user@exam_ple.com",       # underscore in domain is allowed by this function
])
def test_invalid_emails(email):
    assert is_valid_email(email) is False