# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20150515_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='number',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
