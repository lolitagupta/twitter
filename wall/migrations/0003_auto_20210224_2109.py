# Generated by Django 3.1 on 2021-02-24 15:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wall', '0002_followings'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Followings',
            new_name='Following',
        ),
    ]
