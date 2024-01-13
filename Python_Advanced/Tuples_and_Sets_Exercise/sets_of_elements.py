n, m = input().split()

first = set()
second = set()

for _ in range(int(n)):
    first.add(int(input()))

for _ in range(int(m)):
    second.add(int(input()))

print(*first & second, sep='\n')