# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class GrupoSanguineo(models.Model):
	grupo_sanguineo = models.CharField(max_length=255, unique=True, help_text="Escribir un tipo de grupo sanguineo.")