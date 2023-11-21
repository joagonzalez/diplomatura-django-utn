from django.contrib import admin
from dashboards.models import Dashboards, Group



@admin.register(Dashboards)
class DashboardsAdmin(admin.ModelAdmin):
    pass

@admin.register(Group)
class GroupsAdmin(admin.ModelAdmin):
    pass    
