from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Producto, Pais

class productoAdmin(SummernoteModelAdmin):
    list_display = ('producto', 'pais', 'categoria', 'vigente')
    summernote_fields = ('descripcion',)

class paisAdmin(admin.ModelAdmin):
    list_display = ('pais', 'bandera', 'vigente')


admin.site.register(Producto, productoAdmin)
admin.site.register(Pais, paisAdmin)
