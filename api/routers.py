from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def read_root():
    return {'message': 'Start API'}

@router.get('/items/')
async def read_items():
    return {'message': 'Read all items'}

@router.get('/items/{id}')
async def read_item(id: int):
    return {'item_id': id}