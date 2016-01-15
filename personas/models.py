# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from documentos_identificaciones.models import DocumentoIdentificacion
from estados_civiles.models import EstadoCivil

# Create your models here.
class Persona(models.Model):

	BOOL_CHOICES 	 				= ((True, 'Masculino'), (False, "Femenino"))
	nombre 			 		 		= models.CharField(max_length=255, help_text="Escribir nombre(s).")
	apellido_paterno 		 		= models.CharField(max_length=255, help_text="Escribir apellido paterno.")
	apellido_materno 		 		= models.CharField(max_length=255, help_text="Escribir apellido materno.")
	documento_identificacion 		= models.ForeignKey(DocumentoIdentificacion)
	numero_documento_identificacion = models.CharField(max_length=25, help_text="Escribir número documento identificación")
	fecha_nacimiento			    = models.DateField()
	genero 							= models.BooleanField(choices=BOOL_CHOICES)
	estado_civil 					= models.ForeignKey(EstadoCivil)
	grupo_sanguineo 				= models.ForeignKey(GrupoSanguineo)
	fotografia 						= models.ImageField(blank=True, upload_to="fotografía")
	observacion_persona 			= models.TextField(blank=True, help_text="Escribir observación escribir (Opcional).")
	distrito 						= models.ForeignKey(Distrito)
	zona							= models.ForeignKey(Zona)
	nombre_direccion				= models.CharField(blank=True, max_length=255, help_text="Escribir dirección.")
	departamento					= models.CharField(blank=True, max_length=20)
	piso							= models.CharField(blank=True, max_length=20)
	interior						= models.CharField(blank=True, max_length=20)
	numero 							= models.CharField(blank=True, max_length=20)
	cuadra							= models.CharField(blank=True, max_length=20)
	manzana							= models.CharField(blank=True, max_length=20)
	lote							= models.CharField(blank=True, max_length=20)
	sub_lote						= models.CharField(blank=True, max_length=20)
	denominacion					= models.CharField(blank=True, max_length=255, help_text="Escribir denominación (Opcional).")
	referencia						= models.CharField(blank=True, max_length=255, help_text="Escribir referencia (Opcional).")
	observacion_direccion			= models.CharField(blank=True, max_length=255, help_text="Escribir observación de la dirección (Opcional).")
	telefono_personal				= models.PhoneField(blank=True)
	celular_personal				= models.PhoneField(blank=True)
	e_mail							= models.EmailField(blank=True)
	
