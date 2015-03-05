# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TripShare', '0002_auto_20150304_2133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tripusers',
            name='driver',
        ),
        migrations.RemoveField(
            model_name='tripusers',
            name='usersCar',
        ),
        migrations.AddField(
            model_name='trip',
            name='carOwner',
            field=models.ForeignKey(related_name='carOwner', to='TripShare.UserProfile', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ratings',
            name='rating',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trip',
            name='creator',
            field=models.ForeignKey(related_name='creator', to='TripShare.UserProfile'),
            preserve_default=True,
        ),
    ]
