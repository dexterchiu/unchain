# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-23 04:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('queue', '0007_remove_table_occupant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='seat',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='queue.Table'),
        ),
    ]