from django.db import models

from tienda_suscripcion.models import Tienda
from tienda_almacen.models import Producto

# Create your models here.


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=30,default="")
    nombre = models.CharField(max_length=20, default="")
    lastname = models.CharField(max_length=20, default="")
    direccion = models.CharField(max_length=20, default="")
    creditcard = models.IntegerField(default=0)
    passw = models.CharField(max_length=30, default="")
    email = models.CharField(max_length=20, default="")
    seller = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, default="")
    def ver(self):
        print('Desde Models',self.cedula)
        return self.cedula

    def Httprequest(request,cedula=None):
        if request.method == 'GET':
            cedul = request.GET['cedula']
            return cedul

class Cliente2(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=20)
    seller = models.BooleanField(default=False)
    contra = models.CharField(max_length=20)

    def retorna(self):
        queryset = Cliente2.objects.filter(contra=self.contra)
        
        return 'funciono'


   

class Pedido(models.Model):
    numero_pedido = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, blank=True, on_delete=models.CASCADE)

class Factura(models.Model):
    id_factura = models.IntegerField(primary_key=True)
    date = models.DateField()
    precioTotal = models.BigIntegerField()
    nombre_cliente = models.CharField(max_length=20)
    pedido = models.ForeignKey(Pedido, blank=True, on_delete=models.CASCADE, default=0)


class Envio(models.Model):
    id_envio = models.IntegerField(primary_key=True)
    dir_destino = models.CharField(max_length=30)
    precio_envio = models.IntegerField()
    date = models.DateField()
    hora = models.DateTimeField()
    factura = models.ForeignKey(Factura, blank=True, on_delete=models.CASCADE)

class Venta(models.Model):
    tienday = models.ForeignKey(Tienda, blank=True, on_delete=models.CASCADE)
    productoy = models.ForeignKey(Producto, blank=True, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, blank=True, on_delete=models.CASCADE, default=0)




