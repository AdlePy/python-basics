class User:
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return self.username


class Session:
    def __init__(self, engine):
        self.engine = engine

    def get_user(self, username: str) -> User:
        return User(username=username)


def get_session(engine="engine"):
    return Session(engine)


def get_user_by_username(username: str) -> User:
    session = get_session()
    user = session.get_user(username)
    return user
