n = int(input())

cars = set()

for _ in range(n):
    command, plate_number = input().split(', ')
    if command == 'IN':
        cars.add(plate_number)

    elif command == 'OUT':
        cars.discard(plate_number)

if len(cars) <= 0:
    print('Parking Lot is Empty')
else:
    print('\n'.join(cars))