import requests


def test_status_code(url, status_code):
    assert requests.get(url, verify=False).status_code == status_code
