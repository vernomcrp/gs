# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('license_id', models.TextField(verbose_name='\u0e40\u0e25\u0e02\u0e17\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e19')),
                ('description', models.TextField(null=True, verbose_name='\u0e23\u0e32\u0e22\u0e25\u0e30\u0e40\u0e2d\u0e35\u0e22\u0e14\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e40\u0e15\u0e34\u0e21', blank=True)),
                ('drive_by', models.ForeignKey(verbose_name='\u0e02\u0e31\u0e1a\u0e42\u0e14\u0e22', to='driver.Driver')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
