from django.db import models
from django.db.models.fields import CharField, IntegerField, TextField

# Create your models here.

class Api(models.Model):
    personal_id = models.IntegerField()
    bot_link = CharField(max_length=150,default='http://t.me/bank_for_bot')
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.id)