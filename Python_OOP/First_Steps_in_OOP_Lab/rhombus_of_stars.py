n = int(input())


def print_row(size, row):
    print(" " * (n - row), "* " * row)


def print_upper_rhombus_part(n):
    for row in range(1, n+1):
        print_row(n, row)


def print_lower_rhombus_part(n):
    for row in range(n - 1, 0, - 1):
        print_row(n, row)


def print_rhombus(n):
    print_upper_rhombus_part(n)
    print_lower_rhombus_part(n)


print_rhombus(n)