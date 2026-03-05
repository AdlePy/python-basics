from fastapi import Header, status, HTTPException
from . import crud
from .schemas import User


def get_user_by_auth_token(token: str = Header(..., alias="x-auth-token")) -> User:
    user = crud.get_user_by_token(token=token)

    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid auth token"
    )
