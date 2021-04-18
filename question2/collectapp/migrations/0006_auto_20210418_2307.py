# Generated by Django 3.2 on 2021-04-18 17:37

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('collectapp', '0005_list_mymodelname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='List',
        ),
        migrations.AddField(
            model_name='mymodelname',
            name='list',
            field=django_mysql.models.ListCharField(models.CharField(max_length=10), default=1, max_length=66, size=6),
            preserve_default=False,
        ),
    ]
