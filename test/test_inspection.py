from fastapi.testclient import TestClient

from api.main import api
from api.config import route_prefix

client = TestClient(api)
client.base_url += route_prefix
client.base_url = client.base_url.rstrip("/") + "/"

def test_inspection_headers():
    response = client.get("headers")
    assert response.status_code == 200

def test_inspection_ip():
    response = client.get("ip")
    assert response.status_code == 200
    assert "ip" in response.json()
