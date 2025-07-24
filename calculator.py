class Calculator:
    """
    A simple calculator that performs basic arithmetic operations.
    """

    def add(self, a: float, b: float) -> float:
        self._validate_inputs(a, b)
        return a + b

    def subtract(self, a: float, b: float) -> float:
        self._validate_inputs(a, b)
        return a - b

    def multiply(self, a: float, b: float) -> float:
        self._validate_inputs(a, b)
        return a * b

    def divide(self, a: float, b: float) -> float:
        self._validate_inputs(a, b)
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

    def _validate_inputs(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Inputs must be integers or floats.")
