from calculator.operations import addOperator, subtractOperator, multiplyOperator, divideOperator


class Calculator:
    def __init__(self):
        self.operations = {
            "add": addOperator,
            "subtract": subtractOperator,
            "multiply": multiplyOperator,
            "divide": divideOperator,
        }

    def calculate(self, operation: str, a: float, b: float) -> float:
        if operation not in self.operations:
            raise ValueError("Invalid operation.")
        return self.operations[operation](a, b)
