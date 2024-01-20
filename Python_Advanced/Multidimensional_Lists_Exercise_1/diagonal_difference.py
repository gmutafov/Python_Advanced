# n = int(input())
#
# matrix = [[int(el) for el in input().split()] for _ in range(n)]
#
# primary_sum = 0
# secondary_sum = 0
#
# for i in range(n):
#     primary_sum += matrix[i][i]
#     secondary_sum += matrix[i][n - i - 1]
#
# print(abs(primary_sum- secondary_sum))

n = int(input())

primary_sum, secondary_sum = 0, 0

for i in range(n):
    line = [int(x) for x in input().split()]
    primary_sum += line[i]
    secondary_sum += line[n - i - 1]

print(abs(primary_sum- secondary_sum))
