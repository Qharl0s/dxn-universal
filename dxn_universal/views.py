from django.shortcuts import render
from publicacion.models import Publicacion
from json import dumps

def inicio(request):
  publicaciones = Publicacion.objects.filter(inicio=True, vigente=True).order_by('-id')
  publicaciones_ = []
  for publicacion in publicaciones:
    #publicaciones_.append({'title':publicacion.titulo, 'src': publicacion.imagen.url, 'href':'http://'+request.get_host()+'/publicaciones/'+publicacion.titulo})
    publicaciones_.append({'title':publicacion.titulo, 'src': publicacion.imagen_url, 'href':'http://'+request.get_host()+'/publicaciones/'+publicacion.titulo})
  
  context = {'activo_inicio':True, 'publicaciones_':dumps(publicaciones_)}
  return render(request, 'index.html', context)

def planes(request):
  context = {'activo_planes':True}
  return render(request, 'planes.html', context)

def contactanos(request):
  context = {'activo_contactanos':True}
  return render(request, 'contactanos.html', context)

def modulos(request):
  context = {'activo_modulos':True}
  return render(request, 'modulos.html', context)

def sistema_educativo(request):
  context = {'activo_sistema':True}
  return render(request, 'sistema_educativo.html', context)

def acerca_dxn(request):
  context = {'activo_acercadxn':True}
  return render(request, 'acerca_dxn.html', context)