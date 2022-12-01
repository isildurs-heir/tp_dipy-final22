from django.db import models
import uuid
from datetime import datetime
from django.urls import reverse

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return '%s' %self.nombre

class Talla(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return '%s' %self.nombre

class Color(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return '%s' %self.nombre

class Tipo(models.Model):
    nombre = models.CharField(max_length=20)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return '%s' %self.nombre

class Producto(models.Model):
    foto = models.ImageField(upload_to="ropa")
    nombre = models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=9,decimal_places=2)
    cantidad = models.IntegerField(null=False,blank=False)
    descripcion = models.TextField(max_length=200)
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo,on_delete=models.CASCADE)
    talla = models.ForeignKey(Talla,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    

    class Meta:
        ordering = ['nombre']

    def display_tipo(self):
        return ', '.join(cat.tipo for cat in self.tipo.all())
    
    display_tipo.short_description = 'Tipos'

    def get_absolute_url(self):
        return reverse('producto', args=[str(self.id)])

    def __str__(self):
        return '%s - %s(%s,%s,%s)' %(self.nombre,self.marca,self.tipo,self.talla,self.color)

class Articulo(models.Model):
    codigo = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text="codigo unico")#editable=False)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['codigo']

    def display_producto_nombre(self):
        return '%s - %s(%s,%s,%s)' %(self.producto.nombre,self.producto.marca,self.producto.tipo,self.producto.talla,self.producto.color)
    
    display_producto_nombre.short_description = 'Nombre producto'

    def __str__(self):
        return '%s - %s,%s,%s' %(self.display_producto_nombre(),self.producto.tipo,self.producto.talla,self.producto.color)

class Vendido(models.Model):
    codigo = models.CharField(max_length=100,primary_key=True) #(primary_key=True,default=uuid.uuid4,help_text="codigo unico")#editable=False)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    comprador = models.CharField(max_length=50)
    compradoEl = models.DateField(default = datetime.now())

    class Meta:
        ordering = ['compradoEl']

    def __str__(self):
        return '%s, %s' %(self.producto.__str__(),self.compradoEl)