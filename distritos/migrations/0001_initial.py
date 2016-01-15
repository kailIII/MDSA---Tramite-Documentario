# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-15 04:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('provincias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distrito', models.CharField(help_text='Escribir nombre del distrito.', max_length=255, unique=True)),
                ('imagen', models.ImageField(upload_to='imagenes')),
                ('descripcion', models.TextField(blank=True, help_text='Escribe una descripci\xf3n del distrito.')),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provincias.Provincia')),
            ],
        ),
    ]
