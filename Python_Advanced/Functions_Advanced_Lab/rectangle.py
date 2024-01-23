def rectangle(length, width):
    if not (isinstance(length, int) and isinstance(width, int)):
        return "Enter valid values!"

    def area():
        return length * width

    def perimeter():
        return 2 * (length + width)

    result_string = f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"
    return result_string


print(rectangle(2, 10))