# import json

# import requests.exceptions
# from fastapi.testclient import TestClient
# from mock import patch

# from api.config import route_prefix
# from api.main import api

# client = TestClient(api)
# client.base_url = client.base_url.join(route_prefix.rstrip("/") + "/")


# @patch('requests.get')
# def test_istio_envoy_returns_502_when_endpoint_unreachable(mock_server_response):
#     mock_server_response.side_effect = requests.exceptions.ConnectionError
#     response = client.get("istio/envoy")
#     assert response.status_code == 502
#     assert response.json() == {"message": "Unable to query server information"}


# @patch('requests.get')
# def test_istio_envoy_returns_200_when_endpoint_reachable(mock_server_response):
#     locality_info = {
#         "region": "us-region-2",
#         "zone": "us-region-2c",
#         "sub_zone": "some-zone"
#     }

#     server_info = {
#         "node": {
#             "locality": locality_info,
#         }
#     }

#     json_response = json.dumps(server_info)
#     mock_server_response.return_value.content = json_response

#     response = client.get("istio/envoy")
#     assert response.status_code == 200
#     assert response.json() == {"locality": locality_info}
