from django.contrib import admin
from .models import Consulta


@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'fecha', 'atendida')
    list_filter = ('atendida', 'fecha')
    list_editable = ('atendida',)
    search_fields = ('nombre', 'email', 'mensaje')
    readonly_fields = ('fecha',)