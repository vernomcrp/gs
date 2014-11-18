# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0001_initial'),
        ('vehicle', '0002_auto_20141117_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drive_History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField()),
                ('driver', models.ForeignKey(to='driver.Driver')),
                ('vehicle', models.ForeignKey(to='vehicle.Vehicle')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
