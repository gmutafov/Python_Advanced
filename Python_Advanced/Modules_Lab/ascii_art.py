from pyfiglet import figlet_format


def print_text(some_str):

    text = figlet_format(some_str)
    print(text)


print_text(input())