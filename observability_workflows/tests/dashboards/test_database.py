import pytest
import datetime
from dashboards.models import Product



@pytest.fixture()
def create_product(db):
    product = Product(product="Arroz", publish_date=datetime.datetime.now())
    product.save()
    return product

@pytest.mark.django_db
def test_create_product(create_product):
    product = create_product
    print(product.product)
    assert product.product == "Arroz"
    
@pytest.mark.django_db
def test_change_state(product_1):
    assert product_1.status == "Draft"
    
@pytest.mark.django_db
def test_change_state(product_2):
    print(product_2.product)
    print(product_2.publish_date)
    assert product_2.status == "Retired"