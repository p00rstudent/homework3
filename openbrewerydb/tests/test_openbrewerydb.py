import pytest
import requests


def test_accessibility(base_url):
    res = requests.get(base_url, verify=False)
    assert res.status_code == 200


def test_json(base_url):
    res = requests.get(base_url + '/breweries', verify=False)
    body = res.json()
    assert type(body) is list


@pytest.mark.parametrize('state', ['ohio', 'new_york', 'new mexico'])
def test_states(base_url, state):
    res = requests.get(base_url + '/breweries', verify=False, params={'by_state': state})
    res_json = res.json()
    assert res_json


@pytest.mark.parametrize('page', range(5))
def test_pages(base_url, page):
    res = requests.get(base_url + '/breweries', verify=False, params={'page': page})
    res_json = res.json()
    assert res_json


def test_types(base_url, types):
    for _type in types:
        res = requests.get(base_url + '/breweries', verify=False, params={'by_type': _type})
        res_json = res.json()
        assert type(res_json) is list
