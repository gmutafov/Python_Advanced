first_nums = set(int(x) for x in input().split())
second_nums = set(int(x) for x in input().split())

for _ in range(int(input())):
    first_command, second_command, *data = input().split()

    command = first_command + ' ' + second_command

    if command == 'Add First':
        [first_nums.add(int(el)) for el in data]
    elif command == 'Add Second':
        [second_nums.add(int(el)) for el in data]
    elif command == 'Remove First':
        [first_nums.discard(int(el)) for el in data]
    elif command == 'Remove Second':
        [second_nums.discard(int(el)) for el in data]
    else:
        print(first_nums > second_nums or second_nums > first_nums)

print(*sorted(first_nums), sep=', ')
print(*sorted(second_nums), sep=', ')
