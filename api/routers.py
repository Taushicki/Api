from fastapi import APIRouter
from loging_config import setup_logging
setup_logging()
import logging
from database.operations import get_news, save_news, save_user
from typing import Dict
from models.news import Content
from models.user import User

router = APIRouter()

@router.get('/')
async def read_root():
    return {'message': 'Start API'}

@router.get('/items/{id}')
async def read_item(id: int):
    return {'item_id': id}

@router.post('/upload_data')
async def upload_data(data: Dict[str, Content]):
    try:
        for key in data.keys():
            await save_news(key, data[key])
        return {'message': 'Data uploaded successfully'}
    except Exception as error:
        logging.error(error, exc_info=True)
        return {'message': 'Error'}
        
@router.get('/news')
async def get_offset_news(start: int, end: int):
    return await get_news(start, end) 


@router.post('/add_user')
async def add_user(login: str, password: str):
    try:
        await save_user(User(login=login, password=password))
        return {'message': 'User was added'}
    except:
        return {'message': 'A user with this username already exists'}