class FullColumnError(Exception):
    pass


class InvalidColumnChoice(Exception):
    pass


ROWS = 6
COLS = 7


def print_matrix(board):
    for row in board:
        print(row)


def getting_first_row_index(col_index, board):
    for row_index in range(ROWS-1, -1, -1):
        if board[row_index][col_index] == 0:
            return row_index
    else:
        raise FullColumnError('This column is full, please select another one')


def validate_col_choice(col):
    if 1 <= col <= COLS:
        return True
    raise InvalidColumnChoice()


board = []

for _ in range(ROWS):
    board.append([0 for _ in range(COLS)])

turns = 1
while True:
    player = 2 if turns % 2 == 0 else 1

    try:
        column = int(input(f'Player {player}, please choose a column'))
        validate_col_choice(column)
        column_index = int(column) - 1
        row = getting_first_row_index(column_index, board)
        board[row][column_index] = player

    except FullColumnError as ex:
        print(str(ex))
        continue
    except (InvalidColumnChoice, ValueError):
        print(f'This column is invalid, please select a number between 1 and {COLS}')
        continue

    print_matrix(board)
    turns += 1

