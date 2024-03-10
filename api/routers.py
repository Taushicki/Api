from database.models import News
from fastapi import APIRouter
from database.operations import get_news
from database.models import News

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

@router.get('/news')
async def get_offset_news(start: int, end: int):
    return await get_news(start, end) 