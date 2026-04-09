import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file), '../app')))
from app import app
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_health_check(client):
    """System ayakta mı"""
    res = client.get('/health')
    assert res.status_code == 200
    assert res.get_json()['status'] == 'healthy'

def test_get_bikes(client):
    """Bisiklet listesi geliyor mu?"""
    res = client.get('/bikes')
    assert res.status_code == 200
    assert len(res.get_json()) > 0