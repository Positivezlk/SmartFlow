from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

from src.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)


def create_token(sub: str, refresh: bool = False) -> str:
    secret = settings.jwt_refresh_secret if refresh else settings.jwt_secret
    exp = datetime.utcnow() + timedelta(days=7 if refresh else 1)
    return jwt.encode({"sub": sub, "exp": exp}, secret, algorithm="HS256")
