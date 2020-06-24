import unittest

import responses

from dnsimple.response import Response
from dnsimple.struct import Domain
from tests.helpers import DNSimpleTest, DNSimpleMockResponse


class DomainsTest(DNSimpleTest):
    @responses.activate
    def test_list_domains(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/domains',
                                           fixture_name='listDomains/success'))
        domains = self.domains.list_domains(1010).data
        self.assertEqual(2, len(domains))
        self.assertIsInstance(domains[1], Domain)

    @responses.activate
    def test_list_domains_supports_sorting(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/domains?sort=expiration:asc',
                                           fixture_name='listDomains/success'))
        self.domains.list_domains(1010, sort='expiration:asc')

    @responses.activate
    def test_list_domains_supports_filtering(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/domains?name_like=example',
                                           fixture_name='listDomains/success'))
        self.domains.list_domains(1010, filter={'name_like': 'example'})

    @responses.activate
    def test_list_domains_supports_pagination(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/domains?page=2&per_page=1',
                                           fixture_name='listDomains/success'))
        self.domains.list_domains(1010, page=2, per_page=1)

    @responses.activate
    def test_create_domain(self):
        responses.add(DNSimpleMockResponse(method=responses.POST,
                                           path='/1010/domains',
                                           fixture_name='createDomain/created'))
        domain = self.domains.create_domain(1010, 'example-beta.com').data
        self.assertEqual(1, domain.id)
        self.assertEqual('example-alpha.com', domain.name)
        self.assertIsInstance(domain, Domain)

    @responses.activate
    def test_retrieves_a_domain(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/domains/1',
                                           fixture_name='getDomain/success'))
        domain = self.domains.get_domain(1010, 1).data

        self.assertEqual('example-alpha.com', domain.name)

    @responses.activate
    def test_deletes_a_domain(self):
        responses.add(DNSimpleMockResponse(method=responses.DELETE,
                                           path='/1010/domains/1',
                                           fixture_name='deleteDomain/success'))
        response = self.domains.delete_domain(1010, 1)

        self.assertIsInstance(response, Response)
        self.assertEqual(3990, response.rate_limit_remaining)


if __name__ == '__main__':
    unittest.main()
