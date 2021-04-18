# Generated by Django 3.2 on 2021-04-18 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectapp', '0006_auto_20210418_2307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mymodelname',
            old_name='cur',
            new_name='x',
        ),
        migrations.RemoveField(
            model_name='mymodelname',
            name='list',
        ),
        migrations.RemoveField(
            model_name='mymodelname',
            name='strength',
        ),
        migrations.AddField(
            model_name='mymodelname',
            name='y',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mymodelname',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]