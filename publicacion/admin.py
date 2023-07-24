from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Publicacion


class publicacionAdmin(SummernoteModelAdmin):
    list_display = ('titulo', 'inicio', 'vigente')
    summernote_fields = ('contenido',)

admin.site.register(Publicacion, publicacionAdmin)
