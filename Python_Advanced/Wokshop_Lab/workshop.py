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


def travel_direction(coordinates, curr_row, curr_col, element, board):
    count = 0
    row_direct, col_direct = coordinates
    for i in range(1, 4):
        next_el_row_index = curr_row + row_direct * i
        next_el_col_index = curr_col + col_direct * i
        try:
            if board[next_el_row_index][next_el_col_index] == element:
                count += 1
            else:
                return count
        except IndexError:
            return count


def travel_opposite_direction(coordinates, curr_row, curr_col, element, board):
    count = 0
    row_direct, col_direct = coordinates
    for i in range(1, 4):
        next_el_row_index = curr_row - row_direct * i
        next_el_col_index = curr_col - col_direct * i
        try:
            if board[next_el_row_index][next_el_col_index] == element:
                count += 1
            else:
                return count
        except IndexError:
            return count


def is_winner(row_index, col_index, board):
    for direction, coords in DIRECTIONS.items():
        searched_el = board[row_index][col_index]
        travel_direction_count = travel_direction(coords, row_index, col_index, searched_el, board)
        travel_opposite_direction_count = travel_opposite_direction(coords, row_index, col_index, searched_el, board)
        if travel_direction_count + travel_opposite_direction_count + 1 >= 4:
            return True
    else:
        return False


def print_board(board):
    for row in board:
        print(row)


def validate_column_choice(col):
    if 1 <= col <= COLS:
        return True
    raise InvalidColumnChoice


def get_first_available_row(col_index, board):
    for row_index in range(ROWS - 1, -1, -1):
        if board[row_index][col_index] == 0:
            return row_index
    else:
        raise FullColumnError


board = []

for _ in range(ROWS):
    board.append([0 for _ in range(COLS)])

turns = 1

while True:
    player = 2 if turns % 2 == 0 else 1

    try:
        column = int(input(f"Player {player}, please choose a column: "))
        validate_column_choice(column)
        column_index = int(column) - 1
        row = get_first_available_row(column_index, board)
        board[row][column_index] = player
        if is_winner(row, column_index, board):
            break
    except FullColumnError as ex:
        print(f"This column is full, please select another one")
        continue
    except (InvalidColumnChoice, ValueError):
        print(f"This column is invalid, please select a number between 1 and {COLS}")
        continue

    print_board(board)
    turns += 1

print_board(board)
print(f"WINNER is Player {player}")
