from django import forms
from inventario.models import *


class ProductoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
            model = Producto
            fields = ('marca','nombre','descripcion','tipo','talla','color','precio','cantidad','foto')


class ArticuloForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codigo'].disabled = True

    class Meta:
        model = Articulo
        fields = ('codigo', 'producto')

    def clean(self):
        super(ArticuloForm,self).clean()
        producto = self.cleaned_data.get('producto')
        if producto.cantidad == 0:
            self.errors['producto'] = self.error_class(['El producto seleccionado se encuentra sin stock'])
        else:
            cntArticulos = Articulo.objects.all().filter(producto = producto).count()
            if cntArticulos == producto.cantidad:
                self.errors['producto'] = self.error_class(['La cantidad de articulos disponibles no puede superar la cantidad del producto en stock'])
        return self.cleaned_data
    
class VendidoForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['compradoEl'].disabled = True

    class Meta:
        model = Vendido
        fields = ('comprador','compradoEl')
    

    
