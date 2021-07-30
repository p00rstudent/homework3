from pathlib import Path

import pytest
from csv import reader


@pytest.fixture(scope="session")
def base_url():
    return 'https://api.openbrewerydb.org'


@pytest.fixture(scope="session")
def types():
    with Path(__file__).parent.parent.joinpath('src', 'types.csv').open('r') as f:
        return list(reader(f))[0]
