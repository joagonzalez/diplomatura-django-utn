import pytest



@pytest.mark.backend
def test_backend_1():
    assert 1 == 1
    
@pytest.mark.backend
def test_backend_2(database_data):
    assert database_data == 2
