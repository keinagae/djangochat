# Generated by Django 3.1.1 on 2020-09-15 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_conversiontoken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversiontoken',
            name='conversion',
        ),
    ]