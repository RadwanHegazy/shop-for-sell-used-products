# Generated by Django 3.2.6 on 2021-09-27 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_delete_saved'),
        ('user_profile', '0002_profile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='user_saved_products', to='products.Product'),
        ),
    ]
