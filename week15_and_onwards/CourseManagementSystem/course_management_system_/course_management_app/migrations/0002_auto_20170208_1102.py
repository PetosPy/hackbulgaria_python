# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 11:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_management_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lecture',
            options={'ordering': ('week',)},
        ),
        migrations.AlterUniqueTogether(
            name='lecture',
            unique_together=set([('course', 'name')]),
        ),
    ]