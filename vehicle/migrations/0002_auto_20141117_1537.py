# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0001_initial'),
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='drive_by',
            field=models.ForeignKey(default=datetime.datetime(2014, 11, 17, 15, 37, 23, 95911, tzinfo=utc), verbose_name='\u0e02\u0e31\u0e1a\u0e42\u0e14\u0e22', to='driver.Driver'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='description',
            field=models.TextField(null=True, verbose_name='\u0e23\u0e32\u0e22\u0e25\u0e30\u0e40\u0e2d\u0e35\u0e22\u0e14\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e40\u0e15\u0e34\u0e21', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='license_id',
            field=models.TextField(verbose_name='\u0e40\u0e25\u0e02\u0e17\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e19'),
            preserve_default=True,
        ),
    ]
