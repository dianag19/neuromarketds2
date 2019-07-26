from django.db import models

# Create your models here.

class Tienda(models.Model):
    id_tienda = models.IntegerField(primary_key=True)
    nombre_tienda = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    tienda_lider = models.IntegerField()    
    ingreso = models.BigIntegerField()

class suscripcion(models.Model):
    id_suscripcion = models.IntegerField(primary_key=True)
    tienda = models.ForeignKey(Tienda, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    puntos_tienda = models.IntegerField()
    comision_pago = models.IntegerField()
