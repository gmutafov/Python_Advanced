chemical_elements = set()

n = int(input())

for _ in range(n):
    chemicals = input().split()
    for el in chemicals:
        chemical_elements.add(el)

print(*chemical_elements, sep='\n')