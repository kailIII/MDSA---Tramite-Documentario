# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-15 04:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provincia', models.CharField(help_text='Escribir nombre de la provincia.', max_length=255, unique=True)),
                ('imagen', models.ImageField(upload_to='imagenes')),
                ('descripcion', models.TextField(blank=True, help_text='Escribe una descripci\xf3n de la provincia.')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamentos.Departamento')),
            ],
        ),
    ]
