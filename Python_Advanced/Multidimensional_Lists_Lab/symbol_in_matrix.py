n = int(input())

matrix = []

for _ in range(n):
    matrix.append([x for x in input()])

searched_item = input()
found_item = False

for row_index in range(n):
    if found_item:
        break
    for col_index in range(len(matrix[row_index])):
        if matrix[row_index][col_index] == searched_item:
            print(f"({row_index}, {col_index})")
            found_item = True
            break

if not found_item:
    print(f"{searched_item} does not occur in the matrix")