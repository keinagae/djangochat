# Generated by Django 3.1.1 on 2020-09-15 09:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0004_remove_conversiontoken_conversion'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ConversionToken',
            new_name='WebsocketToken',
        ),
    ]