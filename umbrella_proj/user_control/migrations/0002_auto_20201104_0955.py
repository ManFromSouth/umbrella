# Generated by Django 3.1.2 on 2020-11-04 09:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_control', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserAddresses',
            new_name='UserAddress',
        ),
        migrations.RenameModel(
            old_name='UserPhones',
            new_name='UserPhone',
        ),
    ]
