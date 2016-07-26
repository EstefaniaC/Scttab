# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro_Solicitante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('empresa', models.CharField(max_length=50)),
                ('folio_oficio', models.CharField(max_length=50)),
                ('fecha_recibido', models.DateField()),
                ('asunto', models.TextField(max_length=200)),
                ('modalidad', models.CharField(max_length=50)),
                ('numero_registro', models.IntegerField()),
                ('municipio', models.CharField(max_length=50)),
                ('coordinador', models.CharField(max_length=50)),
                ('fecha_entrega_DGTEC', models.DateField()),
                ('observacion', models.TextField(max_length=200)),
            ],
        ),
    ]
