from django.db.models.base import Model
from django.urls import reverse
from django.contrib import sitemaps



class DashboardsSiteMap(sitemaps.Sitemap):
    priority = 0.9
    change_freq = 'daily'
    
    
    def items(self):
        return ['main', ]

    def location(self, item):
        return reverse(item)