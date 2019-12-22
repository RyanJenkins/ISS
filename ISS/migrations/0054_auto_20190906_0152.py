# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-09-06 01:52


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ISS', '0053_merge_20190430_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='RateLimitedAccess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limit_key', models.CharField(max_length=1024)),
                ('address', models.GenericIPAddressField()),
                ('at', models.DateTimeField(auto_now_add=True)),
                ('expires', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='ipban',
            name='expires',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='poster',
            name='theme',
            field=models.CharField(choices=[(b'&T', b'&T'), (b'bibliotek', b'Bibliotek'), (b'amoled', b'AMOLED')], default=b'&T', max_length=256),
        ),
    ]
