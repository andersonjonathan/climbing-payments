# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_auto_20150424_0114'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyTrip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cost', models.IntegerField(verbose_name=b'kostnad')),
                ('isPayed', models.BooleanField(verbose_name=b'\xc3\xa4r betald')),
                ('payDate', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'datum f\xc3\xb6r betalning')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.CharField(default=datetime.datetime(2015, 4, 25, 21, 38, 15, 248820, tzinfo=utc), max_length=200, verbose_name=b'Telefonnummer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='swish',
            field=models.BooleanField(default=datetime.datetime(2015, 4, 25, 21, 39, 9, 390909, tzinfo=utc), verbose_name=b'har swish'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mytrip',
            name='person',
            field=models.ForeignKey(to='payments.Person'),
        ),
        migrations.AddField(
            model_name='mytrip',
            name='trip',
            field=models.ForeignKey(to='payments.Travel'),
        ),
    ]
