import os

while True:
    line, *info = input().split('-')

    if line == 'Create':
        with open(f'files/{info[0]}', 'w'): pass

    elif line == 'Add':
        with open(f"files/{info[0]}", 'a') as file:
            file.write(f"{info[1]}\n")

    elif line == 'Replace':
        try:
            with open(f'files/{info[0]}', 'r+') as file:
                text = file.read()
                text = text.replace(info[1], info[2])
                file.seek(0)
                file.write(text)
                file.truncate()

        except FileNotFoundError:
            print('An error occurred!')

    elif line == 'Delete':
        try:
            os.remove(f"files/{info[0]}")
        except FileNotFoundError:
            print('An error occurred!')

    elif line == 'End':
        break