from django.urls import path, include
from inventario import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('stock/',views.stock,name='stock'),
    path('vendidos/',views.vendidos,name='vendidos'),
    path('articulos/',views.ArticuloListView.as_view(),name='articulos'),
    path('detalle/',views.listaProductos,name='detalle'),
    path('producto/<int:pk>',views.productoPK,name='producto'),
    path('articulos/new',views.articulo_new,name='articulo_new'),
    path('articulo/venta/<pk>',views.vender_articulo,name='vender_articulo'),
    

    path('stock/delete/<pk>',views.producto_delete,name='producto_delete'),
    path('stock/update/<pk>',views.producto_update,name='producto_update')
]