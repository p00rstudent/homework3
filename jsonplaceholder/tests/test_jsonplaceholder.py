import pytest
import requests
from jsonschema import Draft3Validator, ValidationError


def test_accessibility(base_url):
    res = requests.get(base_url, verify=False)
    assert res.status_code == 200


def test_json(base_url):
    res = requests.get(base_url + '/posts', verify=False)
    body = res.json()
    assert type(body) is list


def test_posts_schema(base_url, schema):
    res = requests.get(base_url + '/posts', verify=False)
    body = res.json()
    for item in body:
        try:
            Draft3Validator(schema).validate(list(item.keys()))
        except ValidationError:
            raise AssertionError('Wrong schema')


@pytest.mark.parametrize('length', range(3))
def test_posts_wrong_schema(base_url, length):
    res = requests.get(base_url + '/posts', verify=False)
    body = res.json()
    item = body[0]
    with pytest.raises(ValidationError):
        Draft3Validator({"maxItems": length}).validate(list(item.keys()))


@pytest.mark.parametrize('title', ['foo1', 'foo2', 'foo3'])
@pytest.mark.parametrize('body', ['bar1', 'bar2', 'bar3'])
@pytest.mark.parametrize('userid', range(3))
def test_post(base_url, title, body, userid):
    res = requests.post(
        base_url + '/posts',
        verify=False,
        json={'title': title, 'body': body, 'userId': userid})
    res_json = res.json()
    assert res_json
