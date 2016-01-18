from django.contrib import admin
from .models import Departamento

# Register your models here.
class DepartamentoAdmin(admin.ModelAdmin):
	pass

admin.site.register(Departamento, DepartamentoAdmin)