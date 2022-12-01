from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from inventario.models import *
from inventario.forms import *
from tienda.models import *
from inventario.filters import FiltroProductos

# Create your views here.

def home(request):
    return render(request,'home.html')

def stock(request):
    productos = Producto.objects.all()

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES)
        if formulario.is_valid():
            producto = formulario.save(commit=False)
            producto.foto = formulario.cleaned_data['foto']
            producto.nombre = formulario.cleaned_data['nombre']
            producto.precio = formulario.cleaned_data['precio']
            producto.cantidad = formulario.cleaned_data['cantidad']
            producto.descripcion = formulario.cleaned_data['descripcion']
            producto.marca = formulario.cleaned_data['marca']
            producto.tipo = formulario.cleaned_data['tipo']
            producto.talla = formulario.cleaned_data['talla']
            producto.color = formulario.cleaned_data['color']
            producto.save()
            return redirect('stock')
    else:
        formulario = ProductoForm()

    return render(request,'stock.html',{'productos':productos,'formulario':formulario})

def vendidos(request):
    vendidos = Vendido.objects.all()
    return render(request,'vendidos.html',{'vendidos':vendidos})

class ArticuloListView(generic.ListView):
    model = Articulo
    paginate_by = 9
    context_object_name = 'articulos'
    queryset = Articulo.objects.all()
    template_name = 'articulos.html'

class ProductListView(generic.ListView):
    model = Producto
    paginate_by = 9
    context_object_name = 'productos'
    queryset = Producto.objects.all()
    template_name = 'detalle.html'

def producto_update(request,pk):
    producto  = get_object_or_404(Producto,pk=pk)
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES,instance=producto)
        if formulario.is_valid():
            producto = formulario.save(commit=False)
            producto.foto = formulario.cleaned_data['foto']
            producto.nombre = formulario.cleaned_data['nombre']
            producto.precio = formulario.cleaned_data['precio']
            producto.cantidad = formulario.cleaned_data['cantidad']
            producto.descripcion = formulario.cleaned_data['descripcion']
            producto.marca = formulario.cleaned_data['marca']
            producto.tipo = formulario.cleaned_data['tipo']
            producto.talla = formulario.cleaned_data['talla']
            producto.color = formulario.cleaned_data['color']
            producto.save()
            return redirect('stock')
    else:
        formulario = ProductoForm(instance=producto)
    return render(request,'producto_update.html',{'producto':producto,'formulario':formulario})


def producto_delete(request,pk):
    producto = get_object_or_404(Producto,pk=pk)
    producto.delete()
    return redirect('stock')

def articulo_new(request):
    if request.method == 'POST':
        formulario = ArticuloForm(request.POST)
        if formulario.is_valid():
            articulo = formulario.save(commit=False)
            articulo.producto = formulario.cleaned_data['producto']
            articulo.save()

            pk = articulo.codigo
            A = Articulo.objects.get(pk=pk)
            tituloItem = articulo.producto.nombre + " - " + articulo.producto.marca.nombre
            #pItem = Item.objects.get(titulo__exact = tituloItem)
            #pItem = get_object_or_404(Item,titulo__exact=tituloItem)
            pItem,created= Item.objects.get_or_create(titulo__exact = tituloItem)
            if created:
                pItem.titulo = tituloItem
                pItem.articulos.add(A)
            else:
                pItem.articulos.add(A)
            pItem.save()
            
            return redirect('articulos')
    else:
        formulario = ArticuloForm()
    return render(request, 'articulo_new.html',{'formulario':formulario})

def vender_articulo(request,pk):
    if request.method == 'POST':
        formulario = VendidoForm(request.POST)
        if formulario.is_valid():
            vendido = formulario.save(commit=False)
            #vendido.articulo = formulario.cleaned_data['articulo']
            vendido.comprador = formulario.cleaned_data['comprador']
            vendido.compradoEl = formulario.cleaned_data['compradoEl']
            articulo = Articulo.objects.get(pk =pk)
            vendido.codigo = articulo.codigo
            vendido.producto = articulo.producto
            vendido.save()

            #consulta
            pk = articulo.producto.id
            producto = Producto.objects.get(pk = pk)
            producto.cantidad -=1
            producto.save()    
            

            tituloItem = vendido.producto.nombre + " - " + articulo.producto.marca.nombre
            pItem = Item.objects.get(titulo__exact = tituloItem)
            pItem.articulos.remove(articulo)
            if pItem.articulos.exists():
                pItem.save()
            else:
                pItem.delete()
            ## consulta
            articulo.delete()

            return redirect('articulos')
    else:
        formulario = VendidoForm()
        articulo = Articulo.objects.get(pk = pk)
    return render(request, 'vender_articulo.html',{'formulario':formulario,'articulo':articulo})

def listaProductos(request):
    productos = Producto.objects.all()

    lista_productos = FiltroProductos(request.GET,queryset=productos)

    context = {
        'lista_productos' : lista_productos
    }

    return render(request,'detalle.html',context)

def productoPK(request,pk):
    producto = Producto.objects.get(pk=pk)
    
    context = {
        'producto':producto
    }

    return render(request,'producto_pk.html',context)