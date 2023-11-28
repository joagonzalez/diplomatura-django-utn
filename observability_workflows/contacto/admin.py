from django.contrib import admin
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


admin.site.register(Consulta, ConsultaAdmin)
