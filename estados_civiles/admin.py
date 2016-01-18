# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import EstadoCivil
# Register your models here.

class EstadoCivilAdmin(admin.ModelAdmin):
	pass

admin.site.register(EstadoCivil, EstadoCivilAdmin)