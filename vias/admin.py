# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Via 

# Register your models here.
class ViaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Via, ViaAdmin)