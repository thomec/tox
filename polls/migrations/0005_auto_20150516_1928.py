# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_remove_vote_question'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['number']},
        ),
        migrations.RemoveField(
            model_name='vote',
            name='answer',
        ),
        migrations.AddField(
            model_name='vote',
            name='answers',
            field=models.ManyToManyField(to='polls.Answer'),
        ),
        migrations.AddField(
            model_name='vote',
            name='questions',
            field=models.ManyToManyField(to='polls.Question'),
        ),
    ]
