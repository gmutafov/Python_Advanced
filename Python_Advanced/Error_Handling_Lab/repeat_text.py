try:
    some_text = input()
    n = int(input())
    print(some_text * n)
except ValueError:
    print("Variable times must be an integer")