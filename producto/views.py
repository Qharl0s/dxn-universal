from django.shortcuts import render
from .models import Producto, Pais

def productosView(request):
  productos = Producto.objects.filter(vigente=True)
  paises = Pais.objects.filter(vigente=True)

  context = {'productos' : productos, 'paises': paises, 'activo_producto':True}
  return render(request, 'productos.html', context)
