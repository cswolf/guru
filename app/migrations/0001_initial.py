# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enrolment',
            fields=[
                ('unique_id', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.IntegerField(blank=True, null=True)),
                ('dept', models.CharField(blank=True, max_length=4, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'enrolment',
                'managed': False,
            },
        ),
    ]
