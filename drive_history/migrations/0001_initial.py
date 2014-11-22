# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '__first__'),
        ('vehicle', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drive_History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('driver', models.ForeignKey(to='driver.Driver')),
                ('vehicle', models.ForeignKey(related_name=b'route_paths', to='vehicle.Vehicle')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
