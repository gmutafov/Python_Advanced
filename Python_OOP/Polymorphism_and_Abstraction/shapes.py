from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):

    def calculate_perimeter(self):
        return 2 * pi * self.__radius

    def calculate_area(self):
        return pi * self.__radius ** 2

    def __init__(self, radius):
        self.__radius = radius


class Rectangle(Shape):

    def calculate_area(self):
        return self.__width * self.__height

    def calculate_perimeter(self):
        return 2 * self.__width + 2 * self.__height

    def __init__(self, height, width):
        self.__height = height
        self.__width = width


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())
