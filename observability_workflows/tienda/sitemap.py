from django.db.models.base import Model
from dashboards.models import Dashboards
from django.urls import reverse
from django.contrib import sitemaps



class TiendaSiteMap(sitemaps.Sitemap):
    priority = 0.7
    change_freq = 'weekly'
    
    
    def items(self):
        return Dashboards.objects.all()