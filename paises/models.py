# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Pais(models.Model):
	pais 		= models.CharField(max_length=255, unique=True, help_text="Escribir nombre del país.")
	imagen 		= models.ImageField(blank=True, upload_to="imagenes")
	descripcion = models.TextField(blank=True, help_text="Escribe una descripción del pais. (Opcional)")
