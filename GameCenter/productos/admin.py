from django.contrib import admin
from .models import accesoriosXbox
from .models import JuegosXbox
from .models import accesoriosPlayStation
from .models import accesoriosNintendo
from .models import accesoriosPC
# Register your models here.

class AdministrarAccesorios(admin.ModelAdmin):
    readonly_fields = ('created', 'update')
    list_display = ('nombre', 'precio')
    search_fields = ('nombre', 'precio', 'created', 'update')
    date_hierarchy = 'created'
    list_filter = ('nombre','precio')
admin.site.register(accesoriosXbox, AdministrarAccesorios)



class AdministrarJuegosXbox(admin.ModelAdmin):
    readonly_fields = ('created', 'update')
    list_display = ('nombre', 'precio')
    search_fields = ('nombre', 'precio', 'created', 'update')
    date_hierarchy = 'created'
    list_filter = ('nombre','precio')
admin.site.register(JuegosXbox, AdministrarJuegosXbox)

class AdministrarAccesoriosPlayStation(admin.ModelAdmin):
    readonly_fields = ('created', 'update')
    list_display = ('nombre', 'precio')
    search_fields = ('nombre', 'precio', 'created', 'update')
    date_hierarchy = 'created'
    list_filter = ('nombre','precio')
admin.site.register(accesoriosPlayStation, AdministrarAccesoriosPlayStation)

class AdministrarAccesoriosNintendo(admin.ModelAdmin):
    readonly_fields = ('created', 'update')
    list_display = ('nombre', 'precio')
    search_fields = ('nombre', 'precio', 'created', 'update')
    date_hierarchy = 'created'
    list_filter = ('nombre','precio')
admin.site.register(accesoriosNintendo, AdministrarAccesoriosNintendo)

class AdministrarAccesoriosPC(admin.ModelAdmin):
    readonly_fields = ('created', 'update')
    list_display = ('nombre', 'precio')
    search_fields = ('nombre', 'precio', 'created', 'update')
    date_hierarchy = 'created'
    list_filter = ('nombre','precio')
admin.site.register(accesoriosPC, AdministrarAccesoriosPC)



