from database.models import News

async def news_is_exist(news_id):
    return await News.filter(id=news_id).exists()

async def save_news(news_data):
    if not await news_is_exist(news_data['id']):
        news = News(**news_data)
        await news.save()
    
async def get_news(start: int, end: int):
    return await News.filter().offset(start).limit(end - start).values() 
