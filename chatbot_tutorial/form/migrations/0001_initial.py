# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=120)),
                ('details', models.TextField()),
                ('happy', models.BooleanField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
