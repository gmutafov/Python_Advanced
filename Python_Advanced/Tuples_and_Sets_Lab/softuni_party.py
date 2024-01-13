n = int(input())

cars = set()

for _ in range(n):
    command, number = input().split(', ')
    if command == 'IN':
        cars.add(number)
    elif command == 'OUT':
        cars.discard(number)

if len(cars) <= 0:
    print(f"Parking Lot is Empty")
else:
    print('\n'.join(cars))