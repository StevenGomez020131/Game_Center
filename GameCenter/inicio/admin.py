from django.contrib import admin
from .models import contacto

# Register your models here.

class AdministrarContacto(admin.ModelAdmin):
    readonly_fields = ('created','update')
    date_hierarchy = 'created'
admin.site.register(contacto, AdministrarContacto)