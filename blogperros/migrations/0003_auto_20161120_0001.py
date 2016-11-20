# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogperros', '0002_auto_20161119_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='perro',
            name='fecha_nacimiento',
            field=models.DateField(default='2009-05-28'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='persona',
            name='apellido',
            field=models.CharField(max_length=30, default='2009-05-28'),
            preserve_default=False,
        ),
    ]
