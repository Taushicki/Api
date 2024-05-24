from database.models import News, Users, FavoriteNews
from dto.user import User as UserDTO
from dto.user import UserResponse
from dto.favorite_news import FavoriteNews as FavoriteNewsDTO

class UserServices:
    async def user_exists(self, user_id: str = "", login: str = ""):
        if user_id:
            return await Users.filter(user_id=user_id).exists()
        elif login:
            return await Users.filter(login=login).exists()
        return {'Error' : 'User not found'}
    
    async def authentication(self, login: str, password: str):
        if await self.user_exists(login=login):
            user = await Users.filter(login=login).first()
            if user.password == password:
                return UserResponse(id=user.user_id, 
                                    login=user.login,
                                    email=user.email,
                                    rights=user.rights)
            return {'Error' : 'Invalid password!'}
        return {'Error' : 'User not found!'}
        
    async def news_favorite_exists(self, user_id: str, news_id: str):
        return await FavoriteNews.filter(user_id=user_id, news_id=news_id).exists()
    
    async def save_user(self, user: UserDTO):
        if await self.user_exists(login=user.login):
            return {'Error' : 'A user with this logind already exists!'}    
        return await Users.create(**user.dict())
    
    async def delete_user_by_id(self, user_id: str):
        if not await self.user_exists(user_id=user_id):
            return {'Error' : f'User with id: {user_id} not found!'}
        await FavoriteNews.filter(user_id=user_id).delete()
        await Users.filter(user_id=user_id).delete()
        return {"message" : "Successful"}
        
    async def add_favorite_news(self, favorite_news: FavoriteNewsDTO):
        if not await self.news_favorite_exists(user_id=favorite_news.user_id, news_id=favorite_news.news_id):
            user = await Users.get(user_id=favorite_news.user_id)
            news = await News.get(news_id=favorite_news.news_id)
            return await FavoriteNews.create(user_id=user, news_id=news)
        return {'Error' : 'The news has already been added to favorites'}
        
    async def get_offset_favorite_news(self, user_id: str, start: int, end: int):
        return await FavoriteNews.filter(user_id=user_id).offset(start).limit(end - start).values()
            
    async def delete_favorite_news(self, user_id: str, news_id: str):
        if await self.news_favorite_exists(user_id=user_id, news_id=news_id):
            await FavoriteNews.get(user_id=user_id, news_id=news_id).delete()
            return {"message" : "Successful"}
        return {'Error' : 'News not found'}
        
    async def delete_all_favorite_news(self, user_id: str):
        await FavoriteNews.filter(user_id=user_id).delete()
        return {"message" : "Successful"}
        
    async def get_all_users(self):
        return await Users.all()
    
    async def get_user_by_id(self, user_id: str):
        if await self.user_exists(user_id=user_id):
            return await Users.get(user_id=user_id)
        return {'Error' : 'User not found'}
    
userServices = UserServices()