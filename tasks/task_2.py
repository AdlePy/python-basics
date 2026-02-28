from abc import ABC, abstractmethod


# exercise 1
def camel_case_to_snake_case(paramStr: str) -> str:
    if not paramStr:
        return ""

    result = []

    for idx, char in enumerate(paramStr):
        if char.isupper() and idx:
            result.append("_")
        result.append(char.lower())

    return "".join(result)


# exercise 2
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @property
    def fullname(self):
        return f"{self.lastname} {self.firstname}"


# exercise 3
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius**2)

    def perimeter(self):
        return 3.14 * 2 * self.radius


# exercise 4
class SecretResultReached(ValueError):
    pass


def add(a, b):
    result = a + b
    if result == 42:
        raise SecretResultReached("secret result was found")

    return result


# exercise 5
class Screen:
    def __init__(self, diagonal, horizontal_pix, vertical_pix):
        self.diagonal = diagonal
        self.horizontal_pix = horizontal_pix
        self.vertical_pix = vertical_pix
        self.cm_in_inch = 2.54

    @property
    def aspect_ratio(self):
        return self.horizontal_pix / self.vertical_pix

    @property
    def height(self):
        return self.diagonal / ((self.aspect_ratio**2 + 1) ** 0.5)

    @property
    def width(self):
        return self.aspect_ratio * self.height

    @property
    def height_cm(self):
        return self.height * self.cm_in_inch

    @property
    def width_cm(self):
        return self.width * self.cm_in_inch

    @property
    def area(self):
        return self.width * self.height

    @property
    def area_cm(self):
        return self.area * self.cm_in_inch


# exercise 6
def valid_parentheses(paramStr: str) -> bool:
    balance = 0

    for char in paramStr:
        if char == "(":
            balance += 1
        elif char == ")":
            balance -= 1
            if balance < 0:
                return False

    return balance == 0
