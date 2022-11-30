from django.contrib import admin
from inventario.models import *

# Register your models here.

admin.site.register(Marca)
admin.site.register(Tipo)
admin.site.register(Talla)
admin.site.register(Color)

class ProductoAdminView(admin.ModelAdmin):
    list_display = ('nombre','marca','tipo','talla','color','cantidad')
admin.site.register(Producto,ProductoAdminView)

class ArticuloAdminView(admin.ModelAdmin):
    list_display = ('producto','codigo')
admin.site.register(Articulo,ArticuloAdminView)

class VendidoAdminView(admin.ModelAdmin):
    list_display = ('codigo','producto','comprador','compradoEl')
admin.site.register(Vendido,VendidoAdminView)