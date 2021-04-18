from django.db import models
from django_mysql.models import ListCharField
class MyModelName(models.Model):
    id=models.IntegerField(primary_key=True)
    strength=models.IntegerField(default=10)
    cur=models.IntegerField(default=0)
    list=ListCharField(base_field=models.CharField(max_length=10),size=6,max_length=(6 * 11))