# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='placar_time1',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='partida',
            name='placar_time2',
            field=models.IntegerField(blank=True),
        ),
    ]
