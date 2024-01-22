n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

command = input().split()

while command[0] != 'END':
    commands, r, c, num = command[0], int(command[1]), int(command[2]), int(command[3])

    if not (0 <= r < n and 0 <= c < n):
        print(f"Invalid coordinates")

    elif commands == 'Add':
        matrix[r][c] += num
    elif commands == 'Subtract':
        matrix[r][c] -= num

    command = input().split()

[print(*row) for row in matrix]