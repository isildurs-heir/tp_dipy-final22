from django.contrib import admin
from tienda.models import *

# Register your models here.

#admin.site.register(Item)

class ItemAdminView(admin.ModelAdmin):
    list_display = ('titulo',)
admin.site.register(Item,ItemAdminView)


