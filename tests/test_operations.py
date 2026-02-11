import pytest

from calculator.operations import addOperator, subtractOperator, multiplyOperator, divideOperator


@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (2.5, 2.5, 5.0),
])
def test_add(a, b, expected):
    assert addOperator(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (5, 2, 3),
    (0, 5, -5),
])
def test_subtract(a, b, expected):
    assert subtractOperator(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (-1, 5, -5),
])
def test_multiply(a, b, expected):
    assert multiplyOperator(a, b) == expected


def test_divide():
    assert divideOperator(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divideOperator(10, 0)