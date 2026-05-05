
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.database.models import Category

from fastapi import APIRouter

router = APIRouter()


@router.get('')
def list_categories(user_id: int = Query(...), db: Session = Depends(get_db)):
    return db.query(Category).filter(Category.user_id == user_id).all()


@router.post('')
def create_category(payload: dict, db: Session = Depends(get_db)):
    category = Category(**payload)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


@router.patch('/{category_id}')
def update_category(category_id: int, payload: dict, db: Session = Depends(get_db)):
    category = db.get(Category, category_id)
    for k, v in payload.items():
        setattr(category, k, v)
    db.commit()
    db.refresh(category)
    return category


@router.delete('/{category_id}')
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category = db.get(Category, category_id)
    db.delete(category)
    db.commit()

def list_categories():
    return [{'id': 1, 'name': 'Работа'}]


@router.post('')
def create_category(payload: dict):
    return {'id': 2, **payload}


@router.patch('/{category_id}')
def update_category(category_id: int, payload: dict):
    return {'id': category_id, **payload}


@router.delete('/{category_id}')
def delete_category(category_id: int):
    return {'id': category_id, 'deleted': True}
