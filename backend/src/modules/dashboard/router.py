
from datetime import date
from fastapi import APIRouter, Depends, Query
from sqlalchemy import func
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.database.models import Task

from fastapi import APIRouter


router = APIRouter()


@router.get('/stats')
def stats(user_id: int = Query(...), db: Session = Depends(get_db)):
    active = db.query(func.count(Task.id)).filter(Task.user_id == user_id, Task.status != 'Done', Task.deleted_at.is_(None)).scalar()
    completed = db.query(func.count(Task.id)).filter(Task.user_id == user_id, Task.status == 'Done', Task.deleted_at.is_(None)).scalar()
    overdue = db.query(func.count(Task.id)).filter(Task.user_id == user_id, Task.status == 'Overdue', Task.deleted_at.is_(None)).scalar()
    total = max(active + completed, 1)
    return {'active': active, 'completed': completed, 'overdue': overdue, 'completion_rate': round(completed / total * 100, 2)}


@router.get('/today')
def today(user_id: int = Query(...), db: Session = Depends(get_db)):
    d = str(date.today())
    return db.query(Task).filter(Task.user_id == user_id, Task.deadline.like(f'{d}%'), Task.deleted_at.is_(None)).all()


@router.get('/upcoming')
def upcoming(user_id: int = Query(...), db: Session = Depends(get_db)):
    return db.query(Task).filter(Task.user_id == user_id, Task.deleted_at.is_(None)).order_by(Task.deadline.asc()).limit(5).all()

def stats():
    return {'active': 5, 'completed': 12, 'overdue': 2, 'completion_rate': 70}


@router.get('/today')
def today():
    return {'tasks': []}


@router.get('/upcoming')
def upcoming():
    return {'tasks': []}
