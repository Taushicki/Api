from tortoise import fields
from tortoise.models import Model
import uuid

class News(Model):
    news_id: str = fields.TextField(pk=True)
    title: str = fields.TextField()
    link: str = fields.TextField()
    pub_date: str = fields.TextField()
    description: str = fields.TextField()
    category: str = fields.TextField()
    text: str = fields.TextField()
    
    class Meta:
        ordering = ['-pub_date']


class Users(Model):
    user_id: str = fields.UUIDField(pk=True, default=uuid.uuid4)
    login: str = fields.CharField(max_length=20, unique=True)
    password: str = fields.CharField(max_length=20)
    rights: str = fields.CharField(max_length=5, default='user')
    
    
    
class FavoriteNews(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    user_id = fields.ForeignKeyField('models.Users', related_name='favorite_news')
    news_id = fields.ForeignKeyField('models.News', related_name='favorited_by')

    class Meta:
        table = "favorite_news"

    

