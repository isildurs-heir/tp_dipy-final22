from django_filters import FilterSet, CharFilter
import django_filters
from inventario.models import Producto, Tipo
from django import forms

class FiltroProductos(django_filters.FilterSet):
    
    class Meta:
        model = Producto
        fields = {'nombre':['contains'], 'marca': ['exact'], 'color':['exact'], 'talla':['exact'], 'tipo' :['exact']}

