# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-05 08:16


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ISS', '0055_auto_20191214_0554'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='member_view_only',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='forum',
            name='priority',
            field=models.IntegerField(default=0),
        ),
    ]
