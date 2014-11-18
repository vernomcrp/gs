# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drive_history', '0002_auto_20141117_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drive_history',
            name='vehicle',
            field=models.ForeignKey(to='vehicle.Vehicle'),
            preserve_default=True,
        ),
    ]
