# Generated by Django 3.2.8 on 2021-10-12 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(default='2000-10-10'),
        ),
        migrations.AddField(
            model_name='user',
            name='favorite_store',
            field=models.IntegerField(default=0),
        ),
    ]
