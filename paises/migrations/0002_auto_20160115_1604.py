# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-15 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paises', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pais',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='imagenes'),
        ),
    ]