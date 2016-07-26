# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='inicio_sesion',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('apellidos', models.CharField(max_length=30)),
                ('usuario', models.CharField(max_length=10)),
                ('contrasena', models.CharField(max_length=10)),
            ],
        ),
    ]
