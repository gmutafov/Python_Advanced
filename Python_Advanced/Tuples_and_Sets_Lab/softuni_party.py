n = int(input())

reg_nums = set()


for _ in range(n):
    number = input()
    reg_nums.add(number)


number = input()

while number != 'END':
    if number in reg_nums:
        reg_nums.remove(number)
    number = input()

print(len(reg_nums))

for num in sorted(reg_nums):
    print(num)