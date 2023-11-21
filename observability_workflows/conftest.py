import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'observability_workflows.settings')

import django
django.setup()

import pytest
import datetime
from faker import Faker
from django.contrib.auth.models import User
from productos.models import Product, Category

# file to implement test fixtures. Pytest imports them
# automatically
fake = Faker()

@pytest.fixture()
def create_product():
    product = Product(product="Arroz", publish_date=datetime.datetime.now())
    product.save()
    return product

@pytest.fixture(scope="session") # only executed once during the session if called by several tests
def database_data():
    print('fixture loaded')
    return 2

@pytest.fixture()
def create_product_factory():
    category = Category(name="cat1", slug="slug1")
    category.save()
    
    def create_product(
        status="Draft",
        product="Arroz", 
        publish_date=datetime.datetime.now(),
        category=category):
        
        product = Product(
                    status=status,
                    product=product, 
                    publish_date=publish_date,
                    category=category
                )
        
        product.save()
        return product
    
    return create_product

@pytest.fixture()
def product_1(create_product_factory):
    return create_product_factory(
                "Draft",
                "Product 1", 
                datetime.datetime.now(),
            )
    
@pytest.fixture()
def product_2(create_product_factory):
    return create_product_factory(
                "Retired",
                fake.name(), 
                fake.date(),
            )