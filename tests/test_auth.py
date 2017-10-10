import pytest
import os

from .fixtures import *

from dnsimple import DNSimple, DNSimpleException

@pytest.fixture
def credentials_file():
    return os.path.join(os.getcwd(), '.dnsimple')

class TestAuth(object):

    def setup_method(self, method):
        self.remove_credentials_file()

    def teardown_method(self, method):
        self.remove_credentials_file()

    def remove_credentials_file(self):
        try:
            os.remove(credentials_file())
        except:
            pass

    def test_authentication_with_no_credentials_raises(self):
        with pytest.raises(DNSimpleException) as exception:
            client = DNSimple()

        assert 'No authentication details provided.' in str(exception.value)

    def test_authentication_with_invalid_credentials_raises(self):
        with pytest.raises(DNSimpleException) as exception:
            client = DNSimple(username = 'user@host.com', password = 'bogus')
            client.domains()

        assert 'Authentication failed' in str(exception.value)

    def test_basic_authentication_raises_no_exceptions(self):
        client = DNSimple(
            username = os.getenv('DNSIMPLE_EMAIL'),
            password = os.getenv('DNSIMPLE_PASSWORD'),
            sandbox  = True
        )

        client.domains()

    def test_user_token_auth_raises_no_exception(self):
        client = DNSimple(
            email     = os.getenv('DNSIMPLE_EMAIL'),
            api_token = os.getenv('DNSIMPLE_API_TOKEN'),
            sandbox   = True
        )

        client.domains()

    def test_basic_authentication_from_credentials_file_raises_no_exception(self, credentials_file):
        # Create local credentials file
        file = open(credentials_file, 'w')
        file.writelines([
            "[DNSimple]\n",
            "email: {0}\n".format(os.getenv('DNSIMPLE_EMAIL')),
            "api_token: {0}\n".format(os.getenv('DNSIMPLE_API_TOKEN'))
        ])
        file.close()

        client = DNSimple(sandbox = True)

        client.domains()

    @pytest.mark.skip(reason='APIv2 does not support auth by domain token')
    def test_domain_token_auth(self, client):
        domain_name = 'dnsimple-domain-token.test'

        domain = client.add_domain(domain_name)
        assert domain

        token_client = DNSimple(domain_token = domain['domain']['token'], sandbox = True)

        with pytest.raises(DNSimpleException) as exception:
            token_client.domains()

        assert 'Authentication failed' in str(exception.value)
        assert token_client.domain(domain_name)['domain']['name'] == domain_name

        client.delete(domain_name)

        assert len(client.domains()) == 0
