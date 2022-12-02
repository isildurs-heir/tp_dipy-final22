from django.urls import path, include
from django.contrib.auth.decorators import login_required
from inventario import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('stock/', login_required(views.stock), name='stock'),
    path('vendidos/',login_required(views.vendidos), name='vendidos'),
    path('articulos/', login_required(views.ArticuloListView.as_view()), name='articulos'),
    path('detalle/',views.listaProductos,name='detalle'),
    path('producto/<int:pk>', login_required(views.productoPK), name='producto'),
    path('articulos/new', login_required(views.articulo_new), name='articulo_new'),
    path('articulo/venta/<pk>', login_required(views.vender_articulo), name='vender_articulo'),
    

    path('stock/delete/<pk>',login_required(views.producto_delete), name='producto_delete'),
    path('stock/update/<pk>',login_required(views.producto_update), name='producto_update')
]