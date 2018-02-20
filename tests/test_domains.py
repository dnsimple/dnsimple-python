import pytest

from .fixtures import *

from dnsimple import DNSimple, DNSimpleException

class TestDomains(object):

    def test_check_domain(self, client):
        # Ensure invalid domain names cause errors
        with pytest.raises(DNSimpleException) as exception:
            client.check('add.test')

        assert "TLD .TEST is invalid or not supported" in str(exception.value)

        # Check a domain name that is not available
        status = client.check('google.com')

        assert not status['available']

        status = client.check('dnsimple-python-available-domain.com')

        assert status['available']

    def test_add_domain_with_invalid_attributes(self, client):
        with pytest.raises(DNSimpleException) as exception:
            client.add_domain('bog')

        assert 'Validation failed' in str(exception.value)

    def test_listing_domains(self, client):
        assert client.domains() == []

        client.add_domain('add.test')

        assert [d['domain']['name'] for d in client.domains()] == ['add.test']

    def test_get_domain(self, client):
        domain_name = 'add.test'

        # Find by name
        domain = client.domain(domain_name)
        id     = domain['domain']['id']

        token_only_client = token_client(domain)

        assert domain['domain']['name'] == domain_name
        assert token_only_client.domain(domain_name)['domain']['name'] == domain_name

        # Find by ID
        assert client.domain(id)['domain']['name'] == domain_name
        assert token_only_client.domain(id)['domain']['name'] == domain_name

        # Ensure finding missing domain fails
        with pytest.raises(DNSimpleException) as exception:
            client.domain('missing.com')

        assert "Domain `missing.com` not found" in str(exception.value)

    def test_delete_domains(self, client):
        domain = client.add_domain('another.test')
        assert isinstance(domain, dict)

        domain_count = len(client.domains())

        # Test deleting by name
        response = client.delete('add.test')

        assert isinstance(response, dict)
        assert len(response) == 0
        assert len(client.domains()) == (domain_count - 1)

        # Test deleting by ID
        response = client.delete(domain['domain']['id'])

        assert isinstance(response, dict)
        assert len(response) == 0
        assert len(client.domains()) == (domain_count - 2)

        # Ensure deleting non-existent domain by name fails
        with pytest.raises(DNSimpleException) as exception:
            client.delete('unknown.domain')

        assert "Domain `unknown.domain` not found" in str(exception.value)

        # Ensure deleting non-existent domain by ID fails
        with pytest.raises(DNSimpleException) as exception:
            client.delete(9999)

        assert "Domain `9999` not found" in str(exception.value)
