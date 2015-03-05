# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desc', models.CharField(max_length=255)),
                ('source', models.CharField(max_length=30)),
                ('destination', models.CharField(max_length=30)),
                ('pass_num', models.IntegerField(default=0)),
                ('datetime', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TripUsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trip', models.ForeignKey(to='TripShare.Trip')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('driver', models.BooleanField(default=False)),
                ('hasCar', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tripusers',
            name='user',
            field=models.ForeignKey(to='TripShare.UserProfile'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='tripusers',
            unique_together=set([('user', 'trip')]),
        ),
        migrations.AddField(
            model_name='trip',
            name='creator',
            field=models.ForeignKey(to='TripShare.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='requests',
            name='trip',
            field=models.ForeignKey(to='TripShare.Trip'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='requests',
            name='user',
            field=models.ForeignKey(to='TripShare.UserProfile'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='requests',
            unique_together=set([('user', 'trip')]),
        ),
        migrations.AddField(
            model_name='ratings',
            name='userRated',
            field=models.ForeignKey(related_name='rated_user', to='TripShare.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ratings',
            name='userRater',
            field=models.ForeignKey(related_name='rating_user', to='TripShare.UserProfile'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='ratings',
            unique_together=set([('userRater', 'userRated')]),
        ),
    ]
