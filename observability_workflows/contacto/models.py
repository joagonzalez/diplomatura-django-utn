from django.db import models
from datetime import datetime
from django.utils.html import format_html



class Consulta(models.Model): 
    ANSWERED = 'Contestada'
    NOT_ANSWERED = 'No Contestada'
    IN_PROGRESS = 'En Proceso'
    
    STATES = (
        (ANSWERED, 'Contestada'),
        (NOT_ANSWERED, 'No Contestada'),
        (IN_PROGRESS , 'En Proceso'),
    )
    
    name = models.CharField(blank=False , max_length=50, null=True)
    description = models.CharField(blank=True, null=True, max_length=250)
    mail = models.EmailField(max_length=80, blank=True, null=True)
    answer_state = models.CharField(blank=False , max_length=15, null=True, choices=STATES, default=NOT_ANSWERED)
    phone = models.CharField(blank=False , max_length=50, null=True)
    date = models.DateField(datetime.now, blank=True, editable=True)


    def __str__(self):
        return self.name
    
    def answer_state(self):
        if self.answer_state == 'Contestada':
            return format_html('<span style="background-color:#0a0, color:#fff, padding:5px;">{}</span>', self.answer_state)
        elif self.answer_state == 'No Contestada':
            return format_html('<span style="background-color:#a00, color:#fff, padding:5px;">{}</span>', self.answer_state) 
        else:
            return format_html('<span style="background-color:#F0B203, color:#fff, padding:5px;">{}</span>', self.answer_state)


class Respuesta(models.Model):
    query = models.ForeignKey(to=Consulta, blank=True, null=True, on_delete=models.CASCADE)
    answer = models.TextField(blank=False, null=False)
    date = models.DateField(datetime.now, blank=True, editable=True)
    
    def create_message(self):
        query_state = Consulta.objects.get(id=self.query.id)
        query_state.answer_state = 'Contestada'
        # Aca triggereamos logica de eventos antes una respuesta enviada ademas de cambiar el estado
        # como TELEGRAM/EMAIL etc
    
    def save(self, *args, **kwargs): 
        """
        Allows to trigger specific logic in case a new answer is saved on DB
        """
        self.create_message()
        force_update = False
        
        if self.id:
            force_update = True
        super(Respuesta, self).save(force_update=force_update)