from collections import deque

parentheses = input()
que = deque()


def not_balanced():
    print('NO')
    exit()


if not len(parentheses) % 2 == 0:
    not_balanced()


for element in parentheses:
    if element == '{' or element == '(' or element == '[':
        que.append(element)
    else:
        last = que.pop()

        if element == ')':
            if not last == '(':
                not_balanced()

        elif element == ']':
            if not last == '[':
                not_balanced()

        elif element == '}':
            if not last == '{':
                not_balanced()

print("YES")