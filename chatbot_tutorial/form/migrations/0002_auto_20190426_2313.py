# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='happy',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='details',
            field=models.TextField(max_length=40),
        ),
    ]
