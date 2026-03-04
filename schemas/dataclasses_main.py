from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

    def incr(self):
        self.x += 1
        self.y += 1

    def __add__(self, other: "Point"):
        if isinstance(other, Point):
            return Point(x=self.x + other.x, y=self.y + other.y)

        raise TypeError("other should be Point not the other type")


def demo_point():
    p1 = Point(1, 2)
    p2 = Point(3, 4)

    print(p1)
    print(p2)

    p1.x = 4
    p2.y = 3

    print(p1)
    print(p2)


demo_point()
