import math
from math import log

num = int(input())
command = input()

if command == 'natural':
    print(f"{log(num):.2f}")

else:
    print(f"{log(num, int(command)):.2f}")