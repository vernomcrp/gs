# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drive_history', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drive_history',
            name='start_date',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='drive_history',
            name='vehicle',
            field=models.ForeignKey(to='vehicle.Vehicle'),
            preserve_default=True,
        ),
    ]
