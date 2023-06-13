from django.db import models
from django.utils.html import format_html



class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    
    def __str__(self):
        return '%s' % self.name

class Product(models.Model):
    # descriptors
    draft = "Draft"
    published = "Published"
    retired = "Retired"
    
    PRODUCT_APPROVAL = (
        (draft, "Draft"),
        (published, "Published"),
        (retired, "Retired")
    )
    
    status = models.CharField(max_length=10, choices=PRODUCT_APPROVAL, default=draft)
    product = models.CharField(max_length=200)
    publish_date = models.DateTimeField('Publish Date')
    image = models.ImageField(upload_to='producto/%Y/%m/%d', blank=True, null=True)
    category = models.ForeignKey(Category, blank=False, null=True, on_delete=models.CASCADE)
    
    def product_status(self):
        if self.status == 'Retired':
            return format_html("<span style='color: #f00;'>{}</span>", self.status)
        if self.status == 'Draft':
            return format_html("<span style='color: #f0f;'>{}</span>", self.status)
        if self.status == 'Published':
            return format_html("<span style='color: #099;'>{}</span>", self.status)
    
    def __str__(self):
        return self.product + ' ' + str(self.publish_date)