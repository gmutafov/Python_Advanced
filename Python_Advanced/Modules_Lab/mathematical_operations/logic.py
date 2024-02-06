def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def power(num1, num2):
    return num1 ** num2


sign_mapper = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '**': power,
}


def execute_expression(expression):
    num1_str, sign, num2_str = expression.split()
    num1 = float(num1_str)
    num2 = float(num2_str)

    return sign_mapper[sign](num1, num2)
