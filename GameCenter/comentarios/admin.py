from django.contrib import admin
from .models import comentarios
# Register your models here.

class AdministrarComentarios(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre', 'created')
    search_fields = ('nombre', 'created', 'updated')
    date_hierarchy = 'created'
  
admin.site.register(comentarios, AdministrarComentarios)