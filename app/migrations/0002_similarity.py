# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Similarity',
            fields=[
                ('unique_id', models.AutoField(primary_key=True, serialize=False)),
                ('from_class', models.FloatField()),
                ('to_class', models.FloatField()),
                ('score', models.FloatField()),
            ],
            options={
                'managed': False,
                'db_table': 'similarity',
            },
        ),
    ]
