from fastapi import APIRouter
from loging_config import setup_logging
setup_logging()
import logging
from database.services.news import newsServices
from typing import Dict
from dto.news import Content

router = APIRouter()

@router.get('/news')
async def get_offset_news(start: int, end: int):
    return await newsServices.get_offset_news(start=start, end=end)

@router.get('/news/{id}')
async def get_news_by_id(news_id: str):
    return await newsServices.get_news_by_id(news_id=news_id)

@router.post('/upload_data')
async def upload_data(data: Dict[str, Content]):
    try:
        for key in data.keys():
            await newsServices.save_news(key, data[key])
        return {'message': 'Data uploaded successfully'}
    except Exception as error:
        logging.error(error, exc_info=True)
        return {'message': 'Error'}