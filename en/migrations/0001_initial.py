# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-26 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=40)),
                ('meaning_vn', models.CharField(max_length=1024)),
                ('type', models.CharField(max_length=50)),
                ('meaning_en', models.CharField(max_length=1024)),
            ],
        ),
    ]
