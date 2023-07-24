from django.shortcuts import render
from .models import Publicacion

def publicacionesView(request):
  publicaciones = Publicacion.objects.filter(vigente=True).order_by('-id')

  context = {'publicaciones' : publicaciones, 'activo_publicacion':True}
  return render(request, 'publicaciones.html', context)

def publicacionView(request, titulo=""):
  publicacion = Publicacion.objects.get(titulo=titulo)
  publicaciones = Publicacion.objects.filter(vigente=True).order_by('-id')[:5]

  context = {'publicacion' : publicacion, 'publicaciones' : publicaciones, 'activo_publicacion':True}
  return render(request, 'publicacion_detalle.html', context)
