from django import forms
from django.forms import ModelForm
from dashboards.models import Dashboards

class CargarForm(ModelForm):
    class Meta:
        model = Dashboards
        fields = [
            'name',
            'url',
            'dashboard_type',
            'description',
            'status',
            'image',
            'published_date',
        ]
        
    def __init__(self, *args, **kwargs):
        super(CargarForm, self).__init__(*args, **kwargs)        
        
class SearchDashboardForm(forms.Form):
    query = forms.CharField(
        label='Please insert name of the dashbaord you are interested in',
        widget=forms.TextInput(attrs={'size': 32, 'class': 'form-control', 'id': 'autocomplete'})
    )
        