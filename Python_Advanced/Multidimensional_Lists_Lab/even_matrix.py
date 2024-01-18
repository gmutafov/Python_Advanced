rows = int(input())

matrix = []

# for i in range(rows):
#     data = [int(x) for x in input().split(', ')]
#     matrix.append(data)
#
# even_nums = []
#
# for row in matrix:
#     sublist = []
#     for el in row:
#         if el % 2 == 0:
#             sublist.append(el)
#
#     even_nums.append(sublist)
#
# print(even_nums)

for i in range(rows):
    data = [int(x) for x in input().split(', ') if int(x) % 2 == 0]
    matrix.append(data)

print(matrix)