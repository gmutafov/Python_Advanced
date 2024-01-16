from collections import deque
from math import floor

expression = deque(input().split())

index = 0

while index < len(expression):
    el = expression[index]

    if el == '*':
        for _ in range(index - 1):
            expression.appendleft(int(expression.popleft()) * int(expression.popleft()))
    elif el == '/':
        for _ in range(index - 1):
            expression.appendleft(int(expression.popleft()) / int(expression.popleft()))
    elif el == '-':
        for _ in range(index - 1):
            expression.appendleft(int(expression.popleft()) - int(expression.popleft()))
    elif el == '+':
        for _ in range(index - 1):
            expression.appendleft(int(expression.popleft()) + int(expression.popleft()))

    if el in '*/+-':
        del expression[1]
        index = 1

    index += 1

print(floor(int(expression[0])))