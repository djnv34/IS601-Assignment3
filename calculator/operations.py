def addOperator(a: float, b: float) -> float:
    return a + b


def subtractOperator(a: float, b: float) -> float:
    return a - b


def multiplyOperator(a: float, b: float) -> float:
    return a * b


def divideOperator(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
