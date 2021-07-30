from pathlib import Path

import pytest
import json


@pytest.fixture(scope="session")
def base_url():
    return 'https://dog.ceo/api'


@pytest.fixture(scope="session")
def subbreeds():
    with Path(__file__).parent.parent.joinpath('src', 'sub-breeds.json').open('r') as f:
        return json.load(f)
