from typing import Tuple


def cookies(presents_left: int, nice_kids: int) -> tuple[int, int]:
    for coordinates in directions.values():
        r = santa_pos[0] + coordinates[0]
        c = santa_pos[1] + coordinates[1]

        if neighbourhood[r][c].isalpha():
            if neighbourhood[r][c] == 'V':
                nice_kids += 1

            neighbourhood[r][c] = '-'
            presents_left -= 1

        if not presents_left:
            break

    return presents_left, nice_kids


presents = int(input())
size = int(input())

santa_pos = []
neighbourhood = []

total_good_kids = 0
good_kids_visited = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    line = input().split()
    neighbourhood.append(line)

    if 'S' in line:
        santa_pos = [row, line.index('S')]
        neighbourhood[row][santa_pos[1]] = '-'

    total_good_kids += line.count('V')

command = input()

while command != 'Christmas morning':
    santa_pos = [
        santa_pos[0] + directions[command][0],
        santa_pos[1] + directions[command][1],
    ]

    house = neighbourhood[santa_pos[0]][santa_pos[1]]

    if house == 'V':
        good_kids_visited += 1
        presents -= 1

    elif house == 'C':
        presents, good_kids_visited = cookies(presents, good_kids_visited)

    neighbourhood[santa_pos[0]][santa_pos[1]] = '-'

    if not presents or good_kids_visited == total_good_kids:
        break

    command = input()

neighbourhood[santa_pos[0]][santa_pos[1]] = 'S'

if not presents and good_kids_visited < total_good_kids:
    print(f"Santa ran out of presents!")

[print(*row) for row in neighbourhood]

if good_kids_visited == total_good_kids:
    print(f"Good job, Santa! {total_good_kids} happy nice kid/s.")
else:
    print(f"No presents for {total_good_kids - good_kids_visited} nice kid/s.")