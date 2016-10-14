# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 14:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('annotation_tool', '0002_auto_20161014_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]