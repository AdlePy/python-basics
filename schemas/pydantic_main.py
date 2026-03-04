from pydantic import BaseModel
from datetime import datetime

class Point(BaseModel):
    x: int
    y: int


class User(BaseModel):
    id: int
    age: int = None
    name: str = "John Doe"
    signup_date: datetime | None = None
    friends: list[int] = []
    active: bool = True


def demo_point():
    p = Point(x=1, y=2)
    print(p)

def demo_user():
    user = User(id=1, age=20)
    print(user)

def main():
    # demo_point()
    demo_user()


if __name__ == "__main__":
    main()
