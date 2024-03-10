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
#     id = fields.IntField(pk=True)
#     name = fields.CharField(max_length=255)
#     code = fields.CharField(max_length=3)

# class ExchangeRate(Model):
#     id = fields.IntField(pk=True)
#     currency = fields.ForeignKeyField('models.Currency', related_name='exchange_rates')
#     date = fields.DateField()
#     rate = fields.DecimalField(max_digits=10, decimal_places=4)
    

