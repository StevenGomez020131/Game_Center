from django.contrib import admin
from .models import accesoriosXbox
from .models import imagenesProductos
from .models import JuegosXbox
# Register your models here.

class AdministrarAccesorios(admin.ModelAdmin):
    readonly_fields = ('created', 'update')
    list_display = ('nombre', 'precio')
    search_fields = ('nombre', 'precio', 'created', 'update')
    date_hierarchy = 'created'
    list_filter = ('nombre','precio')
admin.site.register(accesoriosXbox, AdministrarAccesorios)

class AdministrarImagenes(admin.ModelAdmin):
    readonly_fields = ('created', 'update')
    date_hierarchy = 'created'
admin.site.register(imagenesProductos, AdministrarImagenes)

class AdministrarJuegosXbox(admin.ModelAdmin):
    readonly_fields = ('created', 'update')
    list_display = ('nombre', 'precio')
    search_fields = ('nombre', 'precio', 'created', 'update')
    date_hierarchy = 'created'
    list_filter = ('nombre','precio')
admin.site.register(JuegosXbox, AdministrarJuegosXbox)
