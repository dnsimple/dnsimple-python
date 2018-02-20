import pytest
import os

from dnsimple import DNSimple

@pytest.fixture
def client():
    return DNSimple(
        # email     = os.getenv('DNSIMPLE_EMAIL'),
        api_token = os.getenv('DNSIMPLE_API_TOKEN'),
        sandbox   = True
    )

@pytest.fixture
def token_client(domain):
    # return DNSimple(domain_token = domain['token'], sandbox = True)
    return client()
