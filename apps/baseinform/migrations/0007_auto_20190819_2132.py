# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2019-08-19 21:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseinform', '0006_auto_20190819_2131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='analysis',
            old_name='displacementxz',
            new_name='displacementz',
        ),
    ]
