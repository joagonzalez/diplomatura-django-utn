from django.contrib import admin
from dashboards.models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Relacion", {"fields": ["category"]}),
        ("Datos Generales", {"fields": ["publish_date", "product", "image"]})
    ]
    

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)