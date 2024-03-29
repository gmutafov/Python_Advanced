# worms = [int(x) for x in input().split()]
# holes = [int(x) for x in input().split()]
# matches = 0
# worms_size = len(worms)
#
# while worms and holes:
#     curr_worm = worms[-1]
#     curr_hole = holes[0]
#
#     if curr_worm == curr_hole:
#         worms.pop()
#         holes.pop(0)
#         matches += 1
#     else:
#         worms[-1] -= 3
#         if worms[-1] <= 0:
#             worms.pop()
#         holes.pop(0)
#
# print(f"Matches: {matches}" if matches != 0 else "There are no matches.")
#
# if matches != worms_size:
#     print(f"Worms left: {', '.join(str(x) for x in worms)}" if worms else "Worms left: none")
# else:
#     print("Every worm found a suitable hole!")
#
# print(f"Holes left: {', '.join(str(x) for x in holes)}" if holes else "Holes left: none")
from collections import deque

worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])
matches = 0
all_worms_count = len(worms)

while worms and holes:
    curr_worm = worms[-1]
    curr_hole = holes[0]

    if curr_worm == curr_hole:
        worms.pop()
        holes.popleft()
        matches += 1
    else:
        holes.popleft()
        worms[-1] -= 3
        if worms[-1] <= 0:
            worms.pop()

if matches:
    print(f"Matches: {matches}")
else:
    print('There are no matches')

if not worms and matches == all_worms_count:
    print(f"Every worm found a suitable hole!")
elif not worms and matches != all_worms_count:
    print('Worms left: none')
else:
    print(f"Worms left: {', '.join([str(el) for el in worms])}")

if not holes:
    print('Holes left: none')
else:
    print(f"Holes left: {', '.join([str(el) for el in holes])}")