from django.contrib import admin
from dashboards.models import Dashboards, Group



@admin.register(Dashboards)
class DashboardsAdmin(admin.ModelAdmin):
    pass

@admin.register(Group)
class GroupsAdmin(admin.ModelAdmin):
    pass    

# Register your models here.
#admin.site.register(Product, ProductAdmin)
#admin.site.register(Category, CategoryAdmin)