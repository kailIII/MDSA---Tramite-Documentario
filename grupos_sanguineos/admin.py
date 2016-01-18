# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import GrupoSanguineo

# Register your models here.
class GrupoSanguineoAdmin(admin.ModelAdmin):
	pass 

admin.site.register(GrupoSanguineo, GrupoSanguineoAdmin)