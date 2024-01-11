from collections import deque

pumps_info = deque([[int(x) for x in input().split()] for _ in range(int(input()))])

pumps_info_copy = pumps_info.copy()

gas_in_tank = 0
index = 0

while pumps_info_copy:
    petrol,distance = pumps_info_copy.popleft()

    gas_in_tank += petrol

    if gas_in_tank >= distance:
        gas_in_tank -= distance

    else:
        pumps_info.rotate(-1)
        pumps_info_copy = pumps_info.copy()
        index += 1
        gas_in_tank = 0

print(index)