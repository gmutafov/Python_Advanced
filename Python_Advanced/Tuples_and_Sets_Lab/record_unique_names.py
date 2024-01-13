n = int(input())
names = set()
for _ in range(n):
    name = input()
    if name not in names:
        names.add(name)

print('\n'.join(names))