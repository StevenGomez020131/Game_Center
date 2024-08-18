from django.contrib import admin
from .models import comentarios
from .models import ComentarioContacto
# Register your models here.

class AdministrarComentarios(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre', 'created')
    search_fields = ('nombre', 'created', 'updated')
    date_hierarchy = 'created'
  
admin.site.register(comentarios, AdministrarComentarios)

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
admin.site.register(ComentarioContacto, AdministrarComentariosContacto)