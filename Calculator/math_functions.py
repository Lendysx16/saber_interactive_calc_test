def __add(x: float, y: float) -> float:
    return x + y


def __subtract(x: float, y: float) -> float:
    return x - y


def __divide(x: float, y: float) -> float:
    return x / y


def __multiply(x: float, y: float) -> float:
    return x * y


def __pow(x, y):
    return x ** y


dict_with_functions = {'+': __add, '-': __subtract, '*': __multiply, '/': __divide, '^': __pow}

