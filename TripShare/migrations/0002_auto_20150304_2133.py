# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TripShare', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tripusers',
            name='driver',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tripusers',
            name='usersCar',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='avgRating',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='numRatings',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
