from fastapi import APIRouter, Depends, HTTPException
from jose import jwt
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session

from src.core.config import settings
from src.database.db import get_db
from src.database.models import User
from src.security.auth import create_token, hash_password, verify_password

router = APIRouter()


class RegisterPayload(BaseModel):
    username: str
    email: EmailStr
    password: str


class LoginPayload(BaseModel):
    email: EmailStr
    password: str


@router.post('/register')
def register(payload: RegisterPayload, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == payload.email).first():
        raise HTTPException(400, 'Email уже используется')
    user = User(username=payload.username, email=payload.email, password_hash=hash_password(payload.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return {'id': user.id, 'username': user.username, 'email': user.email}


@router.post('/login')
def login(payload: LoginPayload, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(401, 'Неверные данные')
    return {'access_token': create_token(str(user.id)), 'refresh_token': create_token(str(user.id), refresh=True)}


@router.post('/refresh')
def refresh(payload: dict):
    token = payload.get('refresh_token', '')
    try:
        data = jwt.decode(token, settings.jwt_refresh_secret, algorithms=['HS256'])
        return {'access_token': create_token(data['sub'])}
    except Exception as exc:
        raise HTTPException(401, 'Invalid refresh token') from exc


@router.post('/logout')
def logout():
    return {'message': 'Токены удалены на клиенте'}


@router.get('/me')
def me(user_id: int, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(404, 'User not found')
    return {'id': user.id, 'username': user.username, 'email': user.email, 'avatar': user.avatar}
