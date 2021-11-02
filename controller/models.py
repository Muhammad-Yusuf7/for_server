from typing import Text
from django.db import models

# Create your models here.

class Control(models.Model):
    click_user_id = models.IntegerField()
    out_user_id = models.CharField(max_length=1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,blank=True)