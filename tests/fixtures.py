import pytest
import os

from dnsimple import DNSimple

@pytest.fixture(autouse = True)
def client():
    return DNSimple(
        email     = os.getenv('DNSIMPLE_EMAIL'),
        api_token = os.getenv('DNSIMPLE_API_TOKEN'),
        sandbox   = True
    )

