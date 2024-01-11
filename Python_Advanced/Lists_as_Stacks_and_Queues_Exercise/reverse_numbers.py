# some_numbers = input().split()
#
# while some_numbers:
#     print(some_numbers.pop(), end=' ')
from collections import deque

numbers = deque(input().split())

for _ in range(len(numbers)):
    print(numbers.pop(), end=' ')