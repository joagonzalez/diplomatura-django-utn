from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    
    def __str__(self):
        return '%s' % self.name

class Product(models.Model):
    product = models.CharField(max_length=200)
    publish_date = models.DateTimeField('Publish Date')
    image = models.ImageField(upload_to='producto/%Y/%m/%d', blank=True, null=True)
    category = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.product + ' ' + str(self.publish_date)