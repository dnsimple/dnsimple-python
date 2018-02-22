import pytest
import os

from dnsimple import DNSimple

@pytest.fixture
def client():
    return DNSimple(
        api_token = os.getenv('DNSIMPLE_API_TOKEN'),
        sandbox   = True
    )

@pytest.fixture
def token_client(domain):
    # return DNSimple(domain_token = domain['token'], sandbox = True)
    return client()
