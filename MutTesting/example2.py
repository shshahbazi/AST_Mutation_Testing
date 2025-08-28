def calculator(operator, operand1, operand2):
    result = None

    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        if operand2 != 0:
            result = operand1 / operand2
        else:
            result = "Error: Division by zero!"
    elif operator == '//':
        result = operand1 // operand2
    elif operator == '%':
        result = operand1 % operand2
    elif operator == '**':
        result = operand1 ** operand2

    elif operator == '>>':
        result = operand1 >> operand2
    elif operator == '<<':
        result = operand1 << operand2
    elif operator == '|':
        result = operand1 | operand2
    elif operator == '&':
        result = operand1 & operand2
    elif operator == '^':
        result = operand1 ^ operand2

    return result


# Test


def test_addition():
    assert calculator('+', 3, 5) == 8


def test_subtraction():
    assert calculator('-', 10, 4) == 6


def test_multiplication():
    assert calculator('*', 2, 6) == 12


def test_division():
    assert calculator('/', 8, 4) == 2
    assert calculator('/', 5, 0) == "Error: Division by zero!"


def test_floor_division():
    assert calculator('//', 10, 3) == 3


def test_remainder():
    assert calculator('%', 8, 2) == 0


def test_power():
    assert calculator('**', 10, 3) == 1000


def test_right_shift():
    assert calculator('>>', 20, 5) == 0


def test_left_shift():
    assert calculator('<<', 20, 5) == 640


def test_OR():
    assert calculator('|', 15, 4) == 15


def test_AND():
    assert calculator('&', 15, 4) == 4


def test_XOR():
    assert calculator('^', 10, 3) == 9
