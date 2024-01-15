nums = tuple(float(el) for el in input().split())

same_values = {}

for num in nums:
    if num not in same_values:
        same_values[num] = nums.count(num)

for num, same in same_values.items():
    print(f"{num} - {same} times")