import pytest
from calculator import Calculator

calculator = Calculator()

def test_add():
    assert calculator.add(2, 3) == 5

def test_subtract():
    assert calculator.subtract(10, 4) == 6

def test_multiply():
    assert calculator.multiply(3, 5) == 15

def test_divide():
    assert calculator.divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        calculator.divide(10, 0)

def test_invalid_input_add():
    with pytest.raises(TypeError):
        calculator.add("a", 5)

def test_large_numbers():
    assert calculator.multiply(1e100, 2) == 2e100

def test_negative_numbers():
    assert calculator.subtract(-5, -10) == 5
