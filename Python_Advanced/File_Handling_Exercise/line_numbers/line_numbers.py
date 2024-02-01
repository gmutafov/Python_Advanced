from string import punctuation

with open('files/text.txt') as file:
    text = file.readlines()

output_file = open('files/output.txt', 'w')

for i in range(len(text)):
    letters, marks = 0, 0
    for char in text[i]:
        if char.isalpha():
            letters += 1
        elif char in punctuation:
            marks += 1
    output_file.write(f"Line {i + 1}: {''.join(text[i][:-1])} ({letters})({marks})\n")

output_file.close()