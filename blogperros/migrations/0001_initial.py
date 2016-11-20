# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Perro',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('raza', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('dpi', models.CharField(max_length=13)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='asignacion',
            name='perro',
            field=models.ManyToManyField(to='blogperros.Perro'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='persona',
            field=models.ForeignKey(to='blogperros.Persona'),
        ),
    ]
