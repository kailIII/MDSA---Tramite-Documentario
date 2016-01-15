# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from paises.models import Pais

# Create your models here.
class Departamento(models.Model):
	pais 		 = models.ForeignKey(Pais)
	departamento = models.CharField(max_length=255, unique=True, help_text="Escribir nombre del departamento.")
	imagen 		 = models.ImageField(blank=True, upload_to="imagenes")
	descripcion  = models.TextField(blank=True, help_text="Escribe una descripción del departamento.")