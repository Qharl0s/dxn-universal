import datetime
from django.db import models

class Publicacion(models.Model):
  titulo = models.CharField('Título', max_length=360, default='')
  #imagen = models.ImageField(upload_to='publicacion/imagenes/')
  imagen_url = models.CharField('Url', max_length=1200, default='')
  contenido = models.TextField('Contenido', default='')
  inicio = models.BooleanField('Inicio',default=False)
  vigente = models.BooleanField('Vigente',default=True)
  creado = models.DateTimeField(auto_now_add=True, blank=True)

  def __str__(self):
        return self.titulo
