from fastapi import APIRouter
from loging_config import setup_logging
import logging
from api.handle_error import handle_error
from database.services.user import userServices
from dto.user import User as UserDTO
from dto.favorite_news import FavoriteNews as FavoriteNewsDTO


setup_logging()
router = APIRouter()

@router.get('/get_by_id/{id}')
async def get_user_by_id(id: str):
    try:
        return await userServices.get_user_by_id(id)
    except Exception as error:
        return handle_error(error=error)

@router.get('/authentication')
async def authentication(login: str, password: str):
    try:
        return await userServices.authentication(login=login, password=password)
    except Exception as error:
        return handle_error(error=error)
@router.get('/get_all')
async def get_all_users():
    try:
        return await userServices.get_all_users()
    except Exception as error:
        return handle_error(error=error)
    
@router.get('/get_favorite_news')
async def get_favorite_news(user_id: str, start: int, end: int):
    try:
        return await userServices.get_offset_favorite_news(user_id=user_id, start=start, end=end)
    except Exception as error:
        return handle_error(error=error)

@router.post('/register')
async def register_user(user: UserDTO):
    try:
        return await userServices.save_user(user=user)
    except Exception as error:
        return handle_error(error=error)
    
@router.post('/add_favorite_news')
async def add_favorite_news(data: FavoriteNewsDTO):
    try:
        return await userServices.add_favorite_news(favorite_news=data)
    except Exception as error:
        return handle_error(error=error)

@router.delete('/delete')
async def delete_user_by_id(user_id: str):
    try:
        await userServices.delete_user_by_id(user_id=user_id)
    except Exception as error: 
        return handle_error(error=error)

@router.delete('/delete_favorite_news')
async def delete_favorite_news(user_id: str, news_id: str):
    try:
        return await userServices.delete_favorite_news(user_id=user_id, news_id=news_id)
    except Exception as error:
        return handle_error(error=error)
    
@router.delete('/delete_all_favorite_news')
async def delete_all_favorite_news(user_id: str):
    try:
        return await userServices.delete_all_favorite_news(user_id=user_id)
    except Exception as error:
        return handle_error(error=error)
    
