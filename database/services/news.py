from database.models import News, FavoriteNews
from dto.news import Content
from datetime import datetime

class NewsServices:
    async def news_is_exist(self, news_id):
        return await News.filter(news_id=news_id).exists()

    async def get_news_by_id(self, news_id: str):
        if not await self.news_is_exist(news_id=news_id):
            return {'Error' : f'A news with id: {news_id}, not found!'}
        return await News.get(news_id=news_id).values()

    async def save_news(self, news_id: str, news_data: Content):
        if not await self.news_is_exist(news_id=news_id):
            await News.create(news_id=news_id, 
                              title=news_data.title,
                              link=news_data.link,
                              img=news_data.img,
                              pub_date=datetime.strptime(news_data.pub_date, "%a, %d %b %Y %H:%M:%S %z"),
                              description=news_data.description,
                              category=news_data.category,
                              text=news_data.text)
        
    async def get_offset_news(self, start: int, end: int):
        return await News.filter().offset(start).limit(end - start).values()
    
    async def delete_news_by_id(self, news_id: str):
        if not await self.news_is_exist(news_id=news_id):
            return {'Error' : f'A news with id: {news_id}, not found!'}
        await FavoriteNews.filter(news_id=news_id).delete()
        await News.filter(news_id=news_id).delete()
        return {"message" : "Successful"}

newsServices = NewsServices()