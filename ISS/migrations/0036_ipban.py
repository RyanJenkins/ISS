# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-09 19:32


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ISS', '0035_auto_20170604_0032'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPBan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on', models.GenericIPAddressField(null=True)),
                ('given', models.DateTimeField(auto_now_add=True)),
                ('memo', models.TextField(blank=True, default=b'')),
            ],
        ),
    ]
