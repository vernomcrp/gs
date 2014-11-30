# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='drive_by',
            field=models.ForeignKey(verbose_name='\u0e02\u0e31\u0e1a\u0e42\u0e14\u0e22', blank=True, to='driver.Driver', null=True),
        ),
    ]
