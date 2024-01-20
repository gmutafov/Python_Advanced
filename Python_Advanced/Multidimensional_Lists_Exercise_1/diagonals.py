n = int(input())

matrix = [[int(el) for el in input().split(', ')] for _ in range(n)]

primary_diagonals = [matrix[r][r] for r in range(n)]
second_diagonals = [matrix[r][n - r - 1] for r in range(n)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonals)}. Sum: {sum(primary_diagonals)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in second_diagonals)}. Sum: {sum(second_diagonals)}")