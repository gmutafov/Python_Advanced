row = int(input())

matrix = []

for _ in range(row):
    matrix.append([int(x) for x in input().split()])

total_sum = 0

for row_index in range(row):
    for col_index in range(row):
        if row_index == col_index:
            total_sum += matrix[row_index][col_index]

print(total_sum)