# Generated by Django 3.2.3 on 2021-05-23 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_remove_profile_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='last_request',
            field=models.DateField(auto_now=True),
        ),
    ]
