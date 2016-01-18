# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Pais

# Register your models here.
class PaisAdmin(admin.ModelAdmin):
	pass 

admin.site.register(Pais, PaisAdmin)