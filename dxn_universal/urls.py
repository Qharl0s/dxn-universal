"""dxn_universal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.urls import include
from .views import inicio, planes, contactanos, modulos, sistema_educativo, acerca_dxn
from producto.views import productosView
from publicacion.views import publicacionesView, publicacionView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('acerca-dxn', acerca_dxn, name='acerca-dxn'),
    path('sistema-educativo', sistema_educativo, name='sistema-educativo'),
    path('modulos', modulos, name='modulos'),
    path('productos', productosView, name='productos'),
    path('publicaciones', publicacionesView, name='publicaciones'),
    path('publicaciones/<str:titulo>', publicacionView, name="publicaciones"),
    path('contactanos', contactanos, name='contactanos'),
    path('registrate', planes, name='planes'),
    path('summernote/', include('django_summernote.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
