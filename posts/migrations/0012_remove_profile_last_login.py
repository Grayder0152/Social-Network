# Generated by Django 3.2.3 on 2021-05-23 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_profile_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='last_login',
        ),
    ]
