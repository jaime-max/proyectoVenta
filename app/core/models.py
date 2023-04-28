from django.db import models

# Create your models here.
class tipo(models.Model):
    nombres = models.CharField(max_length=150, verbose_name='Nombres')


    def __str__(self):
        return self.nombres

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['id']
        db_table = 'tipo'


class empleado(models.Model):
    tipoempleado = models.ForeignKey(tipo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    cedula = models.CharField(max_length=150, unique=True, verbose_name='Cedula')
    estado = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar/%y/%m/%d', null=True,blank=True)
    cvitae = models.FileField(upload_to='cvitae/%y/%m/%d', null=True,blank=True)


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural= 'Empleados'
        #nombre de la tabla
        db_table= 'empleado'
        ordering = ['id']