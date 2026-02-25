class Shape:
    def get_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def __str__(self):
        return f"length={self.length} width={self.width}"


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def get_area(self):
        return self.length**2


print(f"{Shape}: {Shape.mro()}")
print(f"{Rectangle}: {Rectangle.mro()}")
print(f"{Square}: {Square.mro()}")

test_rectangle = Rectangle(length=4, width=5)
print(test_rectangle)
print(test_rectangle.get_area())

test_square = Square(length=5)
print(test_square)
print(test_square.get_area())
