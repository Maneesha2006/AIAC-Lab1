import builtins
import pytest
from task_0 import calculator

def run_calculator_with_inputs(inputs):
    """Helper to run calculator() with mocked input and capture output."""
    input_iter = iter(inputs)
    outputs = []

    def mock_input(prompt=''):
        outputs.append(prompt)
        return next(input_iter)

    def mock_print(*args, **kwargs):
        outputs.append(' '.join(str(a) for a in args))

    orig_input = builtins.input
    orig_print = builtins.print
    builtins.input = mock_input
    builtins.print = mock_print
    try:
        calculator()
    finally:
        builtins.input = orig_input
        builtins.print = orig_print
    return outputs

def test_addition():
    out = run_calculator_with_inputs(['1', '5', '3'])
    assert any('5.0 + 3.0 = 8.0' in line for line in out)

def test_subtraction():
    out = run_calculator_with_inputs(['2', '10', '4'])
    assert any('10.0 - 4.0 = 6.0' in line for line in out)

def test_multiplication():
    out = run_calculator_with_inputs(['3', '7', '6'])
    assert any('7.0 * 6.0 = 42.0' in line for line in out)

def test_division():
    out = run_calculator_with_inputs(['4', '8', '2'])
    assert any('8.0 / 2.0 = 4.0' in line for line in out)

def test_division_by_zero():
    out = run_calculator_with_inputs(['4', '5', '0'])
    assert any('Error: Division by zero' in line for line in out)

def test_invalid_choice():
    out = run_calculator_with_inputs(['5'])
    assert any('Invalid input' in line for line in out)

def test_invalid_number_input():
    out = run_calculator_with_inputs(['1', 'abc', '2'])
    assert any('Invalid number input' in line for line in out)