# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-02 00:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0007_auto_20171101_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchitem',
            name='condition',
            field=models.CharField(default=' ', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='searchitem',
            name='location',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='searchitem',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]