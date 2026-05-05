from fastapi import APIRouter

router = APIRouter()


@router.get('')
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
