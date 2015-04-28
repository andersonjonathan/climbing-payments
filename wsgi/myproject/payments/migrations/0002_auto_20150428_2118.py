# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='driver_shall_not_pay',
            field=models.BooleanField(default=False, verbose_name='föraren skall ej vara med och dela på avgiften'),
        ),
        migrations.AlterField(
            model_name='mytrip',
            name='cost',
            field=models.IntegerField(verbose_name='kostnad'),
        ),
        migrations.AlterField(
            model_name='mytrip',
            name='isPayed',
            field=models.BooleanField(default=False, verbose_name='är betald'),
        ),
        migrations.AlterField(
            model_name='mytrip',
            name='payDate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='datum för betalning'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(verbose_name='namn', max_length=200),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(verbose_name='Telefonnummer', max_length=200),
        ),
        migrations.AlterField(
            model_name='person',
            name='swish',
            field=models.BooleanField(default=True, verbose_name='har swish'),
        ),
        migrations.AlterField(
            model_name='place',
            name='fee',
            field=models.IntegerField(verbose_name='kostnad att dela på'),
        ),
        migrations.AlterField(
            model_name='place',
            name='length',
            field=models.IntegerField(verbose_name='sträcka tur och retur i km'),
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(verbose_name='namn', max_length=200),
        ),
        migrations.AlterField(
            model_name='travel',
            name='when',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='datum för resan'),
        ),
    ]
