# Generated by Django 3.2.6 on 2021-09-27 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_ask'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='seen',
            field=models.BooleanField(default=False),
        ),
    ]