# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-06-09 16:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='language',
        ),
    ]