from django.db import models
from datetime import datetime
from core.choices import listaGenero
# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    descripcion = models.CharField(max_length=500, null=True, blank=True, verbose_name='Descripcion')


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

class Producto(models.Model):
    cate = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    imagen = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

class Cliente(models.Model):
    nombres = models.CharField(max_length=150, verbose_name='Nombres')
    apellidos = models.CharField(max_length=150, verbose_name='Apellidos')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Cedula')
    fecha_nac = models.DateField(default=datetime.now, verbose_name='Fecha de Nacimiento')
    sexo = models.CharField(max_length=10, choices=listaGenero, default='masculino',verbose_name='Genero')

    def __str__(self):
        return self.nombres

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    fecha_venta = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cliente.nombres

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cantidad = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9,decimal_places=2)

    def __str__(self):
        return self.producto.nombre

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        ordering = ['id']
