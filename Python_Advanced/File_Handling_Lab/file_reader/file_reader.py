file = open('numbers.txt')

total_sum = 0

for line in file.readlines():
    total_sum += int(line)

print(total_sum)