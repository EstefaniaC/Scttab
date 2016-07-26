# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='oficios',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('numero_oficio', models.IntegerField()),
                ('fecha_entrega_DGTEC', models.DateField()),
                ('observacion', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Registro_Solicitante',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('empresa', models.CharField(max_length=50)),
                ('folio', models.CharField(max_length=50)),
                ('fecha_recibido', models.DateField()),
                ('asunto', models.TextField(max_length=200)),
                ('modalidad', models.CharField(max_length=50)),
            ],
        ),
    ]
