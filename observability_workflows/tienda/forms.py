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