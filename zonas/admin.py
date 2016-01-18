# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Zona 

# Register your models here.
class ZonaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Zona, ZonaAdmin)