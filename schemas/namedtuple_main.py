from collections import namedtuple


User = namedtuple("User", "user_id, age")
print(User)


def demo_user():
    my_user = User(user_id=123, age=20)
    print(f"{my_user}, id: {my_user.user_id}, age: {my_user.age}")


def main():
    demo_user()


if __name__ == "__main__":
    main()
