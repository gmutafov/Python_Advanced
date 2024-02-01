import re
import os

words_path = os.path.join('words.txt')
text_path = os.path.join('input.txt')
output = os.path.join('text.txt')


with open(words_path) as file:
    searched_words_as_str = file.read()
    searched_words = [word.lower() for word in searched_words_as_str.split()]

with open(text_path) as file:
    content = file.read().lower()

word_count = {}

for searched_word in searched_words:
    pattern = re.compile(rf"\b{searched_word}\b")
    result = re.findall(pattern, content)
    word_count[searched_word] = len(result)

sorted_count = sorted(word_count.items(), key=lambda x: -x[1])

with open(output, 'a') as file:
    for key, value in sorted_count:
        file.write(f"{key} - {value}\n")