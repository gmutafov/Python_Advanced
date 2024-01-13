text = tuple(input())
letters = {}

for char in text:
    if char not in letters:
        letters[char] = text.count(char)

for letter, times in sorted(letters.items()):
    print(f"{letter}: {times} time/s")
