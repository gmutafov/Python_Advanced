symbols = ("-", ",", ".", "!", "?")

with open('files/text.txt') as file:
    text = file.readlines()

for row in range(0, len(text), 2):
    for symbol in symbols:
        text[row] = text[row].replace(symbol, '@')

    print(*text[row].split()[::-1])