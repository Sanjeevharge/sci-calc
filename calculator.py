import math

class CalculatorError(Exception):
    pass

class Calculator:
    @staticmethod
    def sqrt(x):
        if x < 0:
            raise CalculatorError("sqrt: negative input")
        return math.sqrt(x)

    @staticmethod
    def factorial(n):
        if not (isinstance(n, int) or (isinstance(n, float) and n.is_integer())):
            raise CalculatorError("factorial: input must be integer")
        n = int(n)
        if n < 0:
            raise CalculatorError("factorial: negative input")
        return math.factorial(n)

    @staticmethod
    def ln(x):
        if x <= 0:
            raise CalculatorError("ln: input must be > 0")
        return math.log(x)

    @staticmethod
    def power(x, b):
        return x ** b

#  testing2
