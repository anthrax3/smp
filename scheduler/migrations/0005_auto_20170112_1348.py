# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0004_auto_20160805_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduledpost',
            name='service',
            field=models.CharField(choices=[('facebook', 'Facebook'), ('twitter', 'Twitter'), ('linkedin_oauth2', 'LinkedIn')], max_length=20),
        ),
    ]
