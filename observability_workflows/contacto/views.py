from django.http import HttpResponse
from django.shortcuts import render
from contacto.forms import ConsultaForm
from django.views.generic import View, FormView


class Contacto(FormView):
    template_name = 'contacto/contacto.html'
    form_class = ConsultaForm
    success_url = 'mensaje_enviado'
    
    def form_valid(self, form: ConsultaForm) -> HttpResponse:
        form.save()
        form.send_email()
        
        return super().form_valid(form)
    
    def form_invalid(self, form: ConsultaForm) -> HttpResponse:
        return super().form_invalid(form)
        
class MensajeEnviado(View):
    template = 'contacto/mensaje_enviado.html'
    
    def get(self, request):
        params = {}
        params['message'] = 'here goes the message'
        params['page'] = 'mensaje_enviado.html'
        return render(request, self.template, params)