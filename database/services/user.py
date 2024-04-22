from database.models import News, Users, FavoriteNews
from dto.user import User
from dto.favorite_news import FavoriteNews as FavoriteNewsDTO


class UserServices:
    async def save_user(self, user: User):
        await Users.create(**user.dict())
        
    async def add_favorite_news(self, favorite_news: FavoriteNewsDTO):
        user = await Users.get(user_id=favorite_news.user_id)
        news = await News.get(news_id=favorite_news.news_id)
        await FavoriteNews.create(user_id=user, news_id=news)
        
    async def get_offset_favorite_news(self, user_id: str, start: int, end: int):
        return await FavoriteNews.filter(user_id=user_id).offset(start).limit(end - start).values()
            
    async def delete_favorite_news(self, user_id: str, news_id: str):
        news = await FavoriteNews.get(user_id=user_id, news_id=news_id)
        await news.delete()
        
    async def delete_all_favorite_news(self, user_id: str):
        await FavoriteNews.filter(user_id=user_id).delete()
        
    async def get_all_users(self):
        return await Users.all()
    
    async def get_user_by_id(self, user_id: str):
        return await Users.get(user_id=user_id)
    
userServices = UserServices()