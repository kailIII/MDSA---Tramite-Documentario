# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Provincia

# Register your models here.
class ProvinciaAdmin(admin.ModelAdmin):
	pass

admin.site.register(Provincia, ProvinciaAdmin)