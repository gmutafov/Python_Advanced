rows = int(input())

matrix = []
for i in range(rows):
    data = [int(x) for x in input().split(', ')]
    matrix.append(data)

filtered_list = []

for row in matrix:
    for el in row:
        filtered_list.append(el)

print(filtered_list)