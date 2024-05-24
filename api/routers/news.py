from fastapi import APIRouter
from loging_config import setup_logging
from api.handle_error import handle_error
setup_logging()
import logging
from database.services.news import newsServices
from typing import Dict
from dto.news import Content, NewsModel
from typing import List

router = APIRouter()

@router.get('/news', response_model=List[NewsModel])
async def get_offset_news(start: int, end: int):
    try:
        return await newsServices.get_offset_news(start=start, end=end)
    except Exception as error:
        handle_error(error=error)

@router.get('/news/{id}')
async def get_news_by_id(news_id: str):
    try:
        return await newsServices.get_news_by_id(news_id=news_id)
    except Exception as error:
        handle_error(error=error)

@router.post('/upload_data')
async def upload_data(data: Dict[str, Content]):
    try:
        for key in data.keys():
            await newsServices.save_news(key, data[key])
        return {'message': 'Data uploaded successfully'}
    except Exception as error:
        handle_error(error=error)
    
@router.delete('/delete')
async def delete_news_by_id(news_id: str):
    try:
        await newsServices.delete_news_by_id(news_id=news_id)
    except Exception as error:
        handle_error(error=error)