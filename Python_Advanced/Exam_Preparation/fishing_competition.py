def get_next_pos(position, direction_mapper, direction, matrix):
    current_row, current_col = pos
    row, col = directions[command]
    new_row = current_row + row
    new_col = current_col + col

    if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix):
        return new_row, new_col

    if new_row < 0:
        new_row = len(matrix) - 1
    elif new_row >= len(matrix):
        new_row = 0

    if new_col < 0:
        new_col = len(matrix) - 1
    elif new_col >= len(matrix):
        new_col = 0

    return new_row, new_col


n = int(input())

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

matrix = []
pos = None

for row_idx in range(n):
    data = list(input())

    if "S" in data:
        current_col = data.index("S")
        pos = [row_idx, current_col]

    matrix.append(data)

command = input()
collected_fish = 0
while command != 'collect the nets':
    curr_row, curr_col = pos
    next_row, next_col = get_next_pos(pos, directions, command, matrix)
    symbol = matrix[next_row][next_col]
    matrix[next_row][next_col] = "S"
    matrix[curr_row][curr_col] = "-"
    pos = [next_row, next_col]

    if symbol.isdigit():
        collected_fish += int(symbol)
    elif symbol == "W":
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the "
              f"ship: [{pos[0]},{pos[1]}]")
        exit()

    command = input()

if collected_fish >= 20:
    print('Success! You managed to reach the quota!')
else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - collected_fish} tons of fish more.")

if collected_fish > 0:
    print(f"Amount of fish caught: {collected_fish} tons.")

for row in matrix:
    print(f"{''.join(row)}")