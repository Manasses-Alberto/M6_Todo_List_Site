# Generated by Django 4.2 on 2023-12-18 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m6_todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='end',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='start',
            field=models.CharField(max_length=18),
        ),
    ]
