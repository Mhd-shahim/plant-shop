# Generated by Django 4.2.10 on 2024-02-26 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plant_main', '0002_wishlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='creared_at',
            new_name='created_at',
        ),
    ]
