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
