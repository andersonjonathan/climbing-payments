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
            model_name='place',
            name='fee',
            field=models.IntegerField(default=0, verbose_name=b'kostnad att dela p\xc3\xa5'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='place',
            name='length',
            field=models.IntegerField(verbose_name=b'str\xc3\xa4cka tur och retur i km'),
        ),
        migrations.AlterField(
            model_name='travel',
            name='when',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'datum f\xc3\xb6r resan'),
        ),
    ]
