rows, cols = [int(x) for x in input().split(', ')]

matrix = []

total = 0

for i in range(rows):
    data_in_rows = [    int(el) for el in input().split(', ')]
    total += sum(data_in_rows)
    matrix.append(data_in_rows)

print(total)
print(matrix)