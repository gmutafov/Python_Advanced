worms = [int(x) for x in input().split()]
holes = [int(x) for x in input().split()]
matches = 0
worms_size = len(worms)

while worms and holes:
    curr_worm = worms[-1]
    curr_hole = holes[0]

    if curr_worm == curr_hole:
        worms.pop()
        holes.pop(0)
        matches += 1
    else:
        worms[-1] -= 3
        if worms[-1] <= 0:
            worms.pop()
        holes.pop(0)

print(f"Matches: {matches}" if matches != 0 else "There are no matches.")

if matches != worms_size:
    print(f"Worms left: {', '.join(str(x) for x in worms)}" if worms else "Worms left: none")
else:
    print("Every worm found a suitable hole!")

print(f"Holes left: {', '.join(str(x) for x in holes)}" if holes else "Holes left: none")
