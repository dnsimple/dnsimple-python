import pytest
import random

from .fixtures import *

from dnsimple import DNSimple, DNSimpleException

_domain_name = None

@pytest.fixture
def domain_name():
    global _domain_name
    if _domain_name is None:
        # Add some random because someone can already register this domain
        _domain_name = 'dnsimple-add-{}.test'.format(random.randint(10000, 99999))
    return _domain_name

@pytest.fixture
def domain(client, domain_name):
    try:
        domain = client.domain(domain_name)
    except:
        domain = client.add_domain(domain_name)

    return domain

class TestRecords(object):

    def record_count(self, client, domain):
        return len(client.records(domain['domain']['id']))

    def find_record(self, client, domain, record_name):
        record  = None
        matches = [r for r in client.records(domain['domain']['id']) if r['record']['name'] == record_name]

        if len(matches) == 1:
            record = matches[0]

        return record

    def test_list_records(self, domain, client, token_client):
        # These are the default records created when a domain is created
        default_record_types = ['SOA', 'NS', 'NS', 'NS', 'NS']

        # Listing by domain name
        records = client.records(domain['domain']['name'])
        assert [r['record']['type'] for r in records] == default_record_types

        records = token_client.records(domain['domain']['name'])
        assert [r['record']['type'] for r in records] == default_record_types

        # Listing by domain ID
        records = client.records(domain['domain']['id'])
        assert [r['record']['type'] for r in records] == default_record_types

        records = token_client.records(domain['domain']['id'])
        assert [r['record']['type'] for r in records] == default_record_types

    def test_adding_records(self, domain, client, token_client):
        start_record_count = self.record_count(client, domain)

        # Add an A record
        record = client.add_record(domain['domain']['name'], {
            'record_type': 'A',
            'name':        '',
            'content':     '192.168.1.2'
        })

        assert isinstance(record, dict)

        assert record['record']['name']    == ''
        assert record['record']['content'] == '192.168.1.2'

        record = token_client.add_record(domain['domain']['name'], {
            'record_type': 'A',
            'name':        'token',
            'content':     '192.168.1.2'
        })

        assert record['record']['name'] == 'token'

        # Add a CNAME record
        record = client.add_record(domain['domain']['id'], {
            'record_type': 'CNAME',
            'name':        'www',
            'content':     domain['domain']['name']
        })

        assert isinstance(record, dict)

        assert record['record']['name']    == 'www'
        assert record['record']['content'] == domain['domain']['name']

        record = token_client.add_record(domain['domain']['id'], {
            'record_type': 'CNAME',
            'name':        'token-cname',
            'content':     'token.{0}'.format(domain['domain']['name'])
        })

        assert record['record']['name'] == 'token-cname'

        # Test adding without parameters causes an error
        with pytest.raises(DNSimpleException) as exception:
            client.add_record(domain['domain']['name'], {})

        assert 'Validation failed' in str(exception.value)

        assert self.record_count(client, domain) == (start_record_count + 4)

    def test_find_record(self, domain, client, token_client):
        www = self.find_record(client, domain, 'www')

        # Test finding by record ID
        assert www
        assert client.record(domain['domain']['id'], www['record']['id']) == www
        assert token_client.record(domain['domain']['id'], www['record']['id']) == www

        # Test that finding a non-existent record fails
        with pytest.raises(DNSimpleException) as exception:
            client.record(domain['domain']['id'], 999999)

        assert 'Record `999999` not found' in str(exception.value)

    def test_deleting_records(self, domain, client, token_client):
        start_record_count = self.record_count(client, domain)

        www_record   = self.find_record(client, domain, 'www')
        token_record = self.find_record(client, domain, 'token')

        # Ensure deleting by record ID works
        result = client.delete_record(domain['domain']['id'], www_record['record']['id'])

        assert isinstance(result, dict)
        assert len(result) == 0

        result = token_client.delete_record(domain['domain']['id'], token_record['record']['id'])

        assert isinstance(result, dict)
        assert len(result) == 0

        # Ensure we can't find by name, and the list is 1 fewer
        assert not self.find_record(client, domain, 'www')
        assert not self.find_record(client, domain, 'token')

        assert self.record_count(client, domain) == (start_record_count - 2)

        # Ensure deleting a non-existent record fails
        with pytest.raises(DNSimpleException) as exception:
            client.delete_record(domain['domain']['id'], 999999)

        assert 'Record `999999` not found' in str(exception.value)
