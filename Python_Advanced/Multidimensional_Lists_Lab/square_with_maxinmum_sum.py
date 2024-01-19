row, col = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(row):
    matrix.append([int(el) for el in input().split(', ')])

max_sum = float('-inf')
sub_matrix = []
total_sum = 0

for row_index in range(row - 1):
    for col_index in range(col - 1):
        current_el = matrix[row_index][col_index]
        next_el = matrix[row_index][col_index + 1]
        el_under = matrix[row_index + 1][col_index]
        el_diagonal = matrix[row_index + 1][col_index + 1]

        total_sum = current_el + next_el + el_under + el_diagonal

        if max_sum < total_sum:
            max_sum = total_sum
            sub_matrix = [[current_el, next_el], [el_under, el_diagonal]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)