# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from departamentos.models import Departamento

# Create your models here.
class Provincia(models.Model):
	departamento = models.ForeignKey(Departamento)
	provincia 	 = models.CharField(max_length=255, unique=True, help_text="Escribir nombre de la provincia.")
	imagen 		 = models.ImageField(blank=True, upload_to="imagenes")
	descripcion  = models.TextField(blank=True, help_text="Escribe una descripción de la provincia.")