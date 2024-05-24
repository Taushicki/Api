from pydantic import BaseModel, Field
from datetime import datetime
import uuid

class Content(BaseModel):
    title: str
    link: str
    img: str
    pub_date: str
    description: str
    category: str
    text: str
    
class NewsModel(BaseModel):
    news_id: str
    title: str
    link: str
    img: str
    pub_date: datetime
    description: str
    category: str
    text: str

    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda dt: dt.strftime('%Y-%m-%d %H:%M:%S%z')
        }