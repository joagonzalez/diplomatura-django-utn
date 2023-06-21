import pytest

@pytest.mark.frontend
def test_frontend_1():
    assert 2 == 2

@pytest.mark.frontend
def test_frontend_2():
    assert 2 == 2