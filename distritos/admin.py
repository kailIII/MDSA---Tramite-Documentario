from django.contrib import admin
from .models import Distrito 

# Register your models here.
class DistritoAdmin(admin.ModelAdmin):
	pass

admin.site.register(Distrito, DistritoAdmin)