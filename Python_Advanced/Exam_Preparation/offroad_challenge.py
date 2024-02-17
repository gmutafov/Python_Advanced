from collections import deque

initial_fuel = [int(x) for x in input().split()]
consumption_indexes = deque(int(x) for x in input().split())
quantities_needed = deque(int(x) for x in input().split())

altitude = 0

while initial_fuel and consumption_indexes and quantities_needed:
    current_fuel = initial_fuel[-1]
    current_consumption = consumption_indexes[0]
    used_fuel = current_fuel - current_consumption
    needed_fuel = quantities_needed[0]
    if used_fuel >= needed_fuel:
        initial_fuel.pop()
        consumption_indexes.popleft()
        quantities_needed.popleft()
        altitude += 1
        print(f"John has reached: Altitude {altitude}")
    else:
        print(f"John did not reach: Altitude {altitude + 1}")
        break

if initial_fuel and altitude:
    print(f"John failed to reach the top.")
    print(f"Reached altitudes: {', '.join([f'Altitude {num}' for num in range(1, altitude + 1)])}")
if initial_fuel and not altitude:
    print(f"John failed to reach the top.")
    print("John didn't reach any altitude.")
if not initial_fuel and not consumption_indexes and not quantities_needed:
    print("John has reached all the altitudes and managed to reach the top!")