# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyTrip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cost', models.IntegerField(verbose_name=b'kostnad')),
                ('isPayed', models.BooleanField(default=False, verbose_name=b'\xc3\xa4r betald')),
                ('payDate', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'datum f\xc3\xb6r betalning')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'namn')),
                ('phone', models.CharField(max_length=200, verbose_name=b'Telefonnummer')),
                ('swish', models.BooleanField(default=True, verbose_name=b'har swish')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'namn')),
                ('length', models.IntegerField(verbose_name=b'str\xc3\xa4cka tur och retur i km')),
                ('fee', models.IntegerField(verbose_name=b'kostnad att dela p\xc3\xa5')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'datum f\xc3\xb6r resan')),
                ('driver', models.ForeignKey(to='payments.Person')),
                ('where', models.ForeignKey(to='payments.Place')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='passenger',
            name='name',
            field=models.ForeignKey(to='payments.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='passenger',
            name='trip',
            field=models.ForeignKey(to='payments.Travel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mytrip',
            name='person',
            field=models.ForeignKey(to='payments.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mytrip',
            name='trip',
            field=models.ForeignKey(to='payments.Travel'),
            preserve_default=True,
        ),
    ]
