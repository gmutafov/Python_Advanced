from collections import deque

names = deque(input().split())
n_tosses = int(input()) - 1

while len(names) > 1:
    names.rotate(-n_tosses)
    remove_kid = names.popleft()
    print(f"Removed {remove_kid}")

print(f"Last is {names.popleft()}")