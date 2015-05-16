# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20150516_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
