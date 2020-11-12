from django.contrib import admin
from .models import Producto
from .models import Cliente
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display  = ['codigo','descripcion','precio','stock','marca']
    list_display_links = ['codigo','descripcion']
    list_filter     = ['codigo']
    search_fields   = ['codigo']


admin.site.register(Producto,ProductoAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display  = ['rut','nombre','correo','telefono']
    list_display_links = ['rut','nombre']
    list_filter     = ['rut']
    search_fields   = ['rut']


admin.site.register(Cliente,ClienteAdmin)