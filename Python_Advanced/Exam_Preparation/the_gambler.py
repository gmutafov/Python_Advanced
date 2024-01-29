def handle_current_position(pos, board, initial, jackpot):
    current_char = board[pos[0]][pos[1]]

    if current_char == 'J':
        initial += 100000
        jackpot = True
    elif current_char == 'W':
        initial += 100
    elif current_char == 'P':
        initial -= 200

    board[pos[0]][pos[1]] = 'G'

    return initial, jackpot


def zero(initial):
    return initial <= 0


def game_over():
    print("Game over! You lost everything!")


def move_gambler(command, pos, board):
    row, col = pos
    board[row][col] = '-'
    if command == "up":
        pos[0] -= 1
    elif command == "down":
        pos[0] += 1
    elif command == "left":
        pos[1] -= 1
    elif command == "right":
        pos[1] += 1

    return pos


def out_of_bounds(pos, size):
    return pos[0] < 0 or pos[0] >= size or pos[1] < 0 or pos[1] >= size


def starting_pos(size, area):
    for i in range(size):
        for j in range(size):
            if area[i][j] == 'G':
                return [i, j]
    return None


def fill_board(size):
    board = []
    for _ in range(size):
        board.append(list(input()))
    return board


size = int(input())
board = fill_board(size)
current_pos = starting_pos(size, board)
initial = 100
jackpot = False

while True:
    if jackpot:
        print("You win the Jackpot!")
        break
    command = input()

    if current_pos:
        current_pos = move_gambler(command, current_pos, board)

    if out_of_bounds(current_pos, size) or zero(initial):
        game_over()
        break
    else:
        initial, jackpot = handle_current_position(current_pos, board, initial, jackpot)

    if command == "end":
        break

if not (out_of_bounds(current_pos, size) or zero(initial)):
    print(f"End of the game. Total amount: {initial}$")
    for row in board:
        print(''.join(row))
