from django import forms
from django.forms import ModelForm
from contacto.models import Consulta
from captcha.fields import CaptchaField


class ConsultaForm(ModelForm):
    """
    La clase form usara el model instanciado y los fields
    indicados para decidir que mostrar y aplicar las validaciones
    correspondientes segun lo indicado en la creación del modelo 
    """
    captcha = CaptchaField()
    
    
    class Meta:
        model = Consulta
        fields = [
            'name',
            'description',
            'mail',
            # 'answer_state',
            'phone',
            # 'date',
        ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['mail'].widget.attrs.update({'class': 'form-control'})
        self.fields['captcha'].widget.attrs.update({'class': 'form-control'})
        
    def send_email(self):
        name = self.cleaned_data['name']
        description = self.cleaned_data['description']
        mail = self.cleaned_data['mail']
        phone = self.cleaned_data['phone']
        # answer_state = self.cleaned_data['answer_state']
        # date = self.cleaned_data['date']
        
        print("Enviando mail!!")

        # add logic to send email