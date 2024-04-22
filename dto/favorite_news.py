from pydantic import BaseModel

class FavoriteNews(BaseModel):
    user_id: str
    news_id: str