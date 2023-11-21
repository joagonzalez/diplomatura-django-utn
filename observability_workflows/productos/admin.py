from django.contrib import admin
from productos.models import Category
from productos.models import Product


# Register your models here.
admin.site.register(Product, admin.ModelAdmin)
admin.site.register(Category, admin.ModelAdmin)