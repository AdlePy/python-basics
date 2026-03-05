from pydantic import BaseModel, Field
from uuid import uuid4


def generate_token() -> str:
    return str(uuid4())


class UserBase(BaseModel):
    username: str = Field(..., example="Adilet")


class UserIn(UserBase):
    pass


class UserOut(UserBase):
    id: int = Field(..., example=123)


class User(UserOut):
    token: str = Field(default_factory=generate_token)
