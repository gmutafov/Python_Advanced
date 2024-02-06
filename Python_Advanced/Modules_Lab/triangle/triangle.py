def print_triangle(number):
    print_top_half(number)
    print_bottom_half(number)


def print_top_half(number):
    for row in range(1, number + 1):
        for num in range(1, row + 1):
            print(num, end=' ')
        print()


def print_bottom_half(number):
    for row in range(number, 0, - 1):
        for num in range(1, row):
            print(num, end=' ')
        print()
