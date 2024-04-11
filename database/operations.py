from database.models import News, Users
from models.news import Content
from models.user import User

async def news_is_exist(news_id):
    return await News.filter(id=news_id).exists()

async def save_news(id: str, news_data: Content):
    if not await news_is_exist(id):
        news = News(id=id, **news_data.dict())
        await news.save()
    
async def get_news(start: int, end: int):
    return await News.filter().offset(start).limit(end - start).values()

async def save_user(user: User):
    await Users(**user.dict()).save()



 
