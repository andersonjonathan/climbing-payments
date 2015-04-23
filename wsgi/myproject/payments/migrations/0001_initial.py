# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'namn')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'namn')),
                ('length', models.IntegerField(verbose_name=b'stracka i km')),
            ],
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'datum for resan')),
                ('driver', models.ForeignKey(to='payments.Person')),
                ('where', models.ForeignKey(to='payments.Place')),
            ],
        ),
        migrations.AddField(
            model_name='passenger',
            name='name',
            field=models.ForeignKey(to='payments.Person'),
        ),
        migrations.AddField(
            model_name='passenger',
            name='trip',
            field=models.ForeignKey(to='payments.Travel'),
        ),
    ]
