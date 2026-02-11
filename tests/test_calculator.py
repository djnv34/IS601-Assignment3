import pytest
from calculator.calculator import Calculator


def test_valid_operation():
    calc = Calculator()
    assert calc.calculate("add", 2, 3) == 5


def test_invalid_operation():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.calculate("power", 2, 3)
