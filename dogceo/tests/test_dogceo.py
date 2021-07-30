import pytest
import requests


def test_accessibility(base_url):
    res = requests.get(base_url, verify=False)
    assert res.status_code == 200


def test_breeds_json(base_url):
    res = requests.get(base_url + '/breeds/list/all', verify=False)
    body = res.json()
    assert type(body) is dict
    assert 'message' in body
    assert body['message']


@pytest.mark.parametrize('breed', ['affenpinscher', 'cattledog', 'maltese'])
def test_breed_in_list(base_url, breed):
    res = requests.get(base_url + '/breeds/list/all', verify=False)
    breeds = res.json().get('message', {})
    assert breed in breeds


@pytest.mark.parametrize('breed', ['affenpinscher', 'cattledog', 'maltese'])
def test_breeds_pictures(base_url, breed):
    res = requests.get(base_url + f'/breed/{breed}/images', verify=False)
    assert res.json()['message']


def test_subbreeds(base_url, subbreeds):
    for breed in subbreeds:
        res = requests.get(base_url + f'/breed/{breed}/list', verify=False)
        assert res.json()['message'] == subbreeds[breed]
