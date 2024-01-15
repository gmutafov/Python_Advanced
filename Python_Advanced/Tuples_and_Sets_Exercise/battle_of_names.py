odd_set = set()
even_set = set()

for row in range(1, int(input()) + 1):
    ascii_sum_of_name = sum(ord(name) for name in input()) // row

    if ascii_sum_of_name % 2 == 0:
        even_set.add(ascii_sum_of_name)

    elif ascii_sum_of_name % 2 != 0:
        odd_set.add(ascii_sum_of_name)


odd_sum, even_sum = sum(odd_set), sum(even_set)

if even_sum == odd_sum:
    print(*odd_set.union(even_set), sep=', ')

elif even_sum < odd_sum:
    print(*odd_set.difference(even_set), sep=', ')

else:
    print(*odd_set.symmetric_difference(even_set), sep=', ')