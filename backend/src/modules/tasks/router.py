
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.database.models import Task

router = APIRouter()


@router.get('')
def list_tasks(user_id: int = Query(...), status: str | None = None, priority: str | None = None, db: Session = Depends(get_db)):
    q = db.query(Task).filter(Task.user_id == user_id, Task.deleted_at.is_(None))
    if status:
        q = q.filter(Task.status == status)
    if priority:
        q = q.filter(Task.priority == priority)
    return q.all()


@router.get('/{task_id}')
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)
    if not task or task.deleted_at:
        raise HTTPException(404, 'Task not found')
    return task


@router.post('')
def create_task(payload: dict, db: Session = Depends(get_db)):
    task = Task(**payload)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@router.patch('/{task_id}')
def update_task(task_id: int, payload: dict, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)
    if not task:
        raise HTTPException(404, 'Task not found')
    for k, v in payload.items():
        setattr(task, k, v)
    db.commit()
    db.refresh(task)
    return task


@router.delete('/{task_id}')
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)
    if not task:
        raise HTTPException(404, 'Task not found')
    task.deleted_at = datetime.utcnow()
    db.commit()
from fastapi import APIRouter

router = APIRouter()
_tasks = []


@router.get('')
def list_tasks():
    return _tasks


@router.get('/{task_id}')
def get_task(task_id: int):
    return {'id': task_id, 'title': 'Task mock'}


@router.post('')
def create_task(payload: dict):
    payload['id'] = len(_tasks) + 1
    _tasks.append(payload)
    return payload


@router.patch('/{task_id}')
def update_task(task_id: int, payload: dict):
    return {'id': task_id, **payload}


@router.delete('/{task_id}')
def delete_task(task_id: int):
    return {'id': task_id, 'deleted': True, 'soft_delete': True}
