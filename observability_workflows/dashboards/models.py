from django.db import models
from django.utils.html import format_html



class Dashboards(models.Model):
    # descriptors
    draft = "Draft"
    published = "Published"
    retired = "Retired"
    custom = "Custom"
    external = "External"
    
    DASHBOARD_STATUS = (
        (draft, "Draft"),
        (published, "Published"),
        (retired, "Retired")
    )
    
    DASHBOARD_TYPE = (
        (custom, "Custom"),
        (external, "External"),
    )
    
    status = models.CharField(max_length=50, choices=DASHBOARD_STATUS, default=draft)
    dashboard_type = models.CharField(max_length=50, choices=DASHBOARD_TYPE, default=custom)
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    published_date = models.DateTimeField('Published Date')

        
    def __str__(self):
        return self.name + ' ' + str(self.dashboard_type)
    
class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    dashboards = models.ManyToManyField(Dashboards)