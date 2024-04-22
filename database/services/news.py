from database.models import News
from dto.news import Content


class NewsServices:
    async def news_is_exist(self, news_id):
        return await News.filter(news_id=news_id).exists()

    async def get_news_by_id(self, news_id: str):
        return await News.get(news_id=news_id).values()

    async def save_news(self, news_id: str, news_data: Content):
        if not await self.news_is_exist(news_id=news_id):
            await News.create(news_id=news_id, **news_data.dict())
        
    async def get_offset_news(self, start: int, end: int):
        return await News.filter().offset(start).limit(end - start).values()

    

newsServices = NewsServices()