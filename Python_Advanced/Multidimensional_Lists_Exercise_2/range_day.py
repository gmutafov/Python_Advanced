from typing import List


def move(direction, steps) -> List[int]:
    r = my_pos[0] + directions[direction][0] * steps
    c = my_pos[1] + directions[direction][1] * steps
    if not (0 <= r < size and 0 <= c < size):
        return my_pos
    if field[r][c] == 'x':
        return my_pos

    return [r, c]


def shoot(direction) -> List[int] or None:
    r = my_pos[0] + directions[direction][0]
    c = my_pos[1] + directions[direction][1]

    while 0 <= r < size and 0 <= c < size:
        if field[r][c] == 'x':
            field[r][c] = '.'
            return [r, c]
        r += directions[direction][0]
        c += directions[direction][1]


size = 5
field = []

targets = 0
targets_hit = 0

target_pos = []
my_pos = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    field.append(input().split())

    if 'A' in field[row]:
        my_pos = [row, field[row].index('A')]

    targets += field[row].count('x')

for _ in range(int(input())):
    command = input().split()

    if command[0] == 'move':
        my_pos = move(command[1], int(command[2]))
    elif command[0] == 'shoot':
        target_down_pos = shoot(command[1])

        if target_down_pos:
            target_pos.append(target_down_pos)
            targets_hit += 1
        if targets_hit == targets:
            print(f"Training completed! All {targets} targets hit.")
            break

if targets_hit < targets:
    print(f"Training not completed! {targets - targets_hit} targets left.")
print(*target_pos, sep='\n')