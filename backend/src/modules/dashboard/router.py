from fastapi import APIRouter

router = APIRouter()


@router.get('/stats')
def stats():
    return {'active': 5, 'completed': 12, 'overdue': 2, 'completion_rate': 70}


@router.get('/today')
def today():
    return {'tasks': []}


@router.get('/upcoming')
def upcoming():
    return {'tasks': []}
