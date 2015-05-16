# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20150516_1928'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['number', 'text']},
        ),
    ]
