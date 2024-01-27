numbers_list = [int(x) for x in input().split(", ")] # new
result = 1

for i in range(len(numbers_list)): # new
    number = numbers_list[i] # new
    if number <= 5: # new
        result *= number
    elif 5 < number <= 10:
        result /= number

print(result) # new
