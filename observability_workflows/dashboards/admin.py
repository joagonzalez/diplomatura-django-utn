from django.contrib import admin
from dashboards.models import Product, Category



class PorductInline(admin.TabularInline):
    model = Product
    extra = 0

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [PorductInline]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Relacion", {"fields": ["category"]}),
        ("Datos Generales", {"fields": ["publish_date", "product", "image", "status"]})
    ]
    
    list_display = ["product", "publish_date", "product_status", "image", "upper_case_name"]
    ordering = ['-publish_date']
    list_filter = ['product', 'publish_date']
    search_fields = ['product', 'product_status']
    list_display_links = ['product', 'product_status']
    
    @admin.display(description='Full Name')
    def upper_case_name(self, obj):
        return ("%s %s" % (obj.product, obj.status)).upper()
    

# Register your models here.
#admin.site.register(Product, ProductAdmin)
#admin.site.register(Category, CategoryAdmin)