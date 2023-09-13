from django.db import models

CATEGORIA = (
    ('Alimentos', 'Alimentos y Bebidas'),
    ('Suplementos', 'Suplementos'),
    ('Cuidado', 'Cuidado Personal'),
    ('Electrodomesticos', 'Electrodomésticos'),
  )

class Producto(models.Model):
  producto = models.CharField('Producto', max_length=360, default='')
  #imagen = models.ImageField(upload_to='producto/imagenes/')
  imagen_url = models.CharField('Url', max_length=1200, default='')
  descripcion = models.TextField('Descripción', default='')
  categoria = models.CharField('Categoría', choices=CATEGORIA, default="Alimentos",  max_length=20)
  pais = models.CharField('Pais', max_length=360, default='peru')
  vigente = models.BooleanField('Vigente',default=True)

  def __str__(self):
        return self.producto

class Pais(models.Model):
  pais = models.CharField('Pais', max_length=360, default='')
  bandera = models.CharField('Bandera', max_length=1200, default='')
  vigente = models.BooleanField('Vigente',default=True)

  def __str__(self):
        return self.pais
