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

# class Weather(Model):
#     pass

# class Currency(Model):
#     pass
    

