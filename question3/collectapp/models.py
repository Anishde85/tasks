from django.db import models
from django_mysql.models import ListCharField
class MyModelName(models.Model):
    x=models.IntegerField(default=0)
    y=models.IntegerField(default=0)