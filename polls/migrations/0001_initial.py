# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('value', models.IntegerField(default=0)),
                ('number', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(help_text='Title', max_length=255, verbose_name='title')),
                ('description', models.CharField(help_text='Description', max_length=4095, verbose_name='description')),
                ('pub_date', models.DateTimeField(verbose_name='date published', auto_now_add=True)),
            ],
            options={
                'ordering': ['pub_date', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('poll', models.ForeignKey(to='polls.Poll')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('timestamp', models.DateTimeField(verbose_name='timestamp', auto_now_add=True)),
                ('answer', models.ForeignKey(to='polls.Answer')),
                ('poll', models.ForeignKey(to='polls.Poll')),
                ('question', models.ForeignKey(to='polls.Question')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='polls.Question'),
        ),
    ]
