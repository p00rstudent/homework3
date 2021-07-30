import pytest


@pytest.fixture(scope="session")
def base_url():
    return 'https://jsonplaceholder.typicode.com'


@pytest.fixture(scope="session")
def schema():
    return {
        "maxItems": 4,
    }
