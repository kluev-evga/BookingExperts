from fastapi import Depends, Request
from jose import ExpiredSignatureError, JWTError, jwt

from app.config import settings
from app.exceptions import (TokenInvalidException, TokenAbsentException, TokenExpiredException)
from app.user.service import UsersService


def get_token(request: Request):
    """Dependency: return token or raise error"""
    token = request.cookies.get("booking_access_token")
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    """
        Dependency: return current user or raise error.
        Accept JWT token from get_token(dependency) and validate it.
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except ExpiredSignatureError:
        raise TokenExpiredException
    except JWTError:
        raise TokenInvalidException

    user_id: str = payload.get("sub")
    if not user_id:
        raise TokenInvalidException
    user = await UsersService.find_one_or_none(id=int(user_id))
    if not user:
        raise TokenInvalidException
    return user