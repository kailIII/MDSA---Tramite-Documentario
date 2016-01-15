# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from provincias.models import Provincia

# Create your models here.
class Distrito(models.Model):
	provincia 	= models.ForeignKey(Provincia)
	distrito 	= models.CharField(max_length=255, unique=True, help_text="Escribir nombre del distrito.")
	imagen 		= models.ImageField(blank=True, upload_to="imagenes")
	descripcion = models.TextField(blank=True, help_text="Escribe una descripción del distrito.")