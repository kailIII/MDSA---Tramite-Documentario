# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class EstadoCivil(models.Model):
	estado_civil = models.CharField(max_length=255, unique=True, help_text="Escribir un tipo de estado civil.")