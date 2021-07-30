import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        type=str,
        help="This is request url"
    )

    parser.addoption(
        "--status_code",
        default=200,
        type=int,
        help="expected status code"
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")
