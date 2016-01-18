# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Persona

# Register your models here.
class PersonaAdmin(admin.ModelAdmin):
	pass

admin.site.register(Persona, PersonaAdmin)


