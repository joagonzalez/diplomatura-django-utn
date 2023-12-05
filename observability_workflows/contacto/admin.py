from django.contrib import admin
from django.core import serializers
from django.http import HttpResponse
from contacto.models import Consulta, Respuesta


class RespuestaAdmin(admin.TabularInline):
    model = Respuesta
    extra = 0

class ConsultaAdmin(admin.ModelAdmin):
    inlines = [RespuestaAdmin]    
    list_display = [
            'answer_state_format', 
            'name',
            'description',
            'mail',
            'phone',
            'date'
            ]
    
    list_filter = ['answer_state', 'date']
    actions = ['export_json']
    
    def export_json(self, request, queryset):
        response = HttpResponse(content_type="application/json")
        serializers.serialize('json', queryset=queryset, stream=response)
        
        return response


admin.site.register(Consulta, ConsultaAdmin)
