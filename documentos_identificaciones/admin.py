# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import DocumentoIdentificacion

# Register your models here.
class DocumentoIdenticacionAdmin(admin.ModelAdmin):
	pass

admin.site.register(DocumentoIdentificacion, DocumentoIdenticacionAdmin)