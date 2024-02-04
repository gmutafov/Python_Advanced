class FullColumnError(Exception):
    pass


class InvalidColumnChoice(Exception):
    pass


ROWS = 6
COLS = 7

DIRECTIONS = {
    'left': (0, -1),
    'up': (-1, 0),
    'main_diagonal': (-1, -1),
    'other_diagonal': (-1, 1),
}


def travel_direction(coordinates, curr_row, curr_col,  el, board):
    count = 0
    for i in range(1, 4):
        row_direction, col_direction = coordinates
        next_el_row_idx = curr_row + row_direction * i
        next_el_col_idx = curr_col + col_direction * i
    try:
        if board[next_el_row_idx][next_el_col_idx] == el:
            count += 1
        else:
            return count
    except IndexError:
        return count


def travel_opposite_direction(coords, curr_row, curr_col, searched_el, board):



def is_winner(curr_row, curr_col, board):
    for direction, coords in DIRECTIONS.items():
        searched_el = board[curr_row][curr_col]
        travel_direct_count = travel_direction(coords, curr_row, curr_col, searched_el, board)
        travel_opposite_direct_count = travel_opposite_direction(coords, curr_row, curr_col, searched_el, board)


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
        if is_winner(row, column_index, board):
            break
    except FullColumnError as ex:
        print(str(ex))
        continue
    except (InvalidColumnChoice, ValueError):
        print(f'This column is invalid, please select a number between 1 and {COLS}')
        continue

    print_matrix(board)
    turns += 1
print(f'WINNER is Player {player}')
print_matrix(board)