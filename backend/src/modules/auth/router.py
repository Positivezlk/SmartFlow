from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

router = APIRouter()


class RegisterPayload(BaseModel):
    username: str
    email: EmailStr
    password: str


class LoginPayload(BaseModel):
    email: EmailStr
    password: str


@router.post('/register')
def register(payload: RegisterPayload):
    return {'message': 'Регистрация выполнена (mock)', 'user': payload.model_dump(exclude={'password'})}


@router.post('/login')
def login(payload: LoginPayload):
    return {'access_token': 'mock-access', 'refresh_token': 'mock-refresh', 'email': payload.email}


@router.post('/refresh')
def refresh():
    return {'access_token': 'mock-access-new'}


@router.post('/logout')
def logout():
    return {'message': 'Выход выполнен'}


@router.get('/me')
def me():
    return {'id': 1, 'username': 'demo', 'email': 'demo@smartflow.ai'}
