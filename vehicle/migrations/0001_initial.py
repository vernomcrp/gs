# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vehicle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('license_id', models.TextField(verbose_name=b'\xe0\xb9\x80\xe0\xb8\xa5\xe0\xb8\x82\xe0\xb8\x97\xe0\xb8\xb0\xe0\xb9\x80\xe0\xb8\x9a\xe0\xb8\xb5\xe0\xb8\xa2\xe0\xb8\x99')),
                ('description', models.TextField(null=True, verbose_name=b'\xe0\xb8\xa3\xe0\xb8\xb2\xe0\xb8\xa2\xe0\xb8\xa5\xe0\xb8\xb0\xe0\xb9\x80\xe0\xb8\xad\xe0\xb8\xb5\xe0\xb8\xa2\xe0\xb8\x94\xe0\xb9\x80\xe0\xb8\x9e\xe0\xb8\xb4\xe0\xb9\x88\xe0\xb8\xa1\xe0\xb9\x80\xe0\xb8\x95\xe0\xb8\xb4\xe0\xb8\xa1', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
