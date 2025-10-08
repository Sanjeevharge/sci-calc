import pytest
from calculator import Calculator, CalculatorError

def test_sqrt():
    assert Calculator.sqrt(9) == 3

def test_factorial():
    assert Calculator.factorial(5) == 120

def test_ln():
    import math
    assert pytest.approx(Calculator.ln(math.e), rel=1e-6) == 1

def test_power():
    assert Calculator.power(2, 3) == 8

def test_factorial_nonint():
    with pytest.raises(CalculatorError):
        Calculator.factorial(3.5)
