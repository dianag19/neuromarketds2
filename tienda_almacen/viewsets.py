from rest_framework import viewsets
from .models import Producto
from .serializer import ProductoSerializer

class ProductoViewSets(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
   
    serializer_class = ProductoSerializer