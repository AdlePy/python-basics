from .schemas import UserIn, User


USER_ID_TO_USER: dict[int, User] = {}
USER_TOKEN_TO_USER: dict[str, User] = {}


def list_users() -> list[User]:
    return list(USER_ID_TO_USER.values())


def create_user(user_in: UserIn) -> User:
    user_id = len(USER_ID_TO_USER) + 1
    user = User(id=user_id, **user_in.model_dump())
    USER_ID_TO_USER[user_id] = user
    return user


def get_user_by_id(user_id: int) -> User | None:
    return USER_ID_TO_USER.get(user_id)


def get_user_by_token(token: str) -> User | None:
    return USER_TOKEN_TO_USER.get(token)
