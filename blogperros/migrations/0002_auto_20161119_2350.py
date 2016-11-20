# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogperros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perro',
            name='imagen',
            field=models.FileField(upload_to='', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='foto',
            field=models.FileField(upload_to='', blank=True, null=True),
        ),
    ]
