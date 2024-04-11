from tortoise import fields
from tortoise.models import Model

class News(Model):
    id: str = fields.TextField(pk=True)
    title: str = fields.TextField()
    link: str = fields.TextField()
    pub_date: str = fields.TextField()
    description: str = fields.TextField()
    category: str = fields.TextField()
    text: str = fields.TextField()
    
    class Meta:
        ordering = ['-pub_date']


class Users(Model):
    id: int = fields.IntField(pk=True)
    login: str = fields.CharField(max_length=20, unique=True)
    password: str = fields.CharField(max_length=20)
    rights: str = fields.CharField(max_length=5, default='user')
    
    
    
class FavoriteNews(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.Users', related_name='favorite_news')
    news = fields.ForeignKeyField('models.News', related_name='favorited_by')

    class Meta:
        table = "favorite_news"

    

