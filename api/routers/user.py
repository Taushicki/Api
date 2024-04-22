from fastapi import APIRouter
from loging_config import setup_logging
setup_logging()
import logging
from database.services.user import userServices
from dto.user import User
from dto.favorite_news import FavoriteNews

router = APIRouter()

@router.get('/get_by_id/{id}')
async def get_user_by_id(id: str):
    try:
        return {'news': await userServices.get_user_by_id(id)}
    except:
        return {'message' : 'News not found'}
    
@router.get('/get_all')
async def get_all_users():
    return await userServices.get_all_users()

@router.get('/get_favorite_news')
async def get_favorite_news(user_id: str, start: int, end: int):
    try:
        return await userServices.get_offset_favorite_news(user_id=user_id, start=start, end=end)
    except Exception as error:
        return {'message' : f'Error {error}'}

@router.post('/register')
async def register_user(login: str, password: str):
    try:
        await userServices.save_user(User(login=login, password=password))
        return {'message': 'User was added'}
    except Exception as error:
        logging.error(error, exc_info=True)
        return {'message': 'A user with this username already exists'}
    
@router.post('/add_favorite_news')
async def add_favorite_news(data: FavoriteNews):
    try:
        await userServices.add_favorite_news(favorite_news=data)
        return {'message' : 'The news was successfully added to favorites'}
    except Exception as error:
        logging.error(error, exc_info=True)
        print(error)
        return {'message' : 'Error adding to favorites'}
    
@router.delete('/delete_favorite_news')
async def delete_favorite_news(user_id: str, news_id: str):
    try:
        await userServices.delete_favorite_news(user_id=user_id, news_id=news_id)
        return {'message' : 'Record deleted sucsessfully'}
    except Exception as error:
        logging.error(error, exc_info=True)
        return {'message': f'Error {error}'}
    
@router.delete('/delete_all_favorite_news')
async def delete_all_favorite_news(user_id: str):
    try:
        await userServices.delete_all_favorite_news(user_id=user_id)
        return {'message' : 'All favorite news was deleted sucsessfully'}
    except Exception as error:
        logging.error(error, exc_info=True)
        return {'message' : f'Error {error}'}