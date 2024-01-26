import unittest

import responses

from dnsimple.client import Client
from tests.helpers import DNSimpleMockResponse, DNSimpleTest


class DnsAnalyticsTest(DNSimpleTest):
    @responses.activate
    def test_dns_analytics(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1/dns_analytics',
                                           fixture_name='dnsAnalytics/success'))
        client = Client(email='tester@example.com', password='secret', base_url='https://api.sandbox.dnsimple.com')
        response = client.dns_analytics.query(1)
        self.assertEqual(12, len(response.data))
        self.assertEqual('2023-12-08', response.data[0].date)

    @responses.activate
    def test_supports_filtering(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1/dns_analytics',
                                           fixture_name='dnsAnalytics/success'))
        client = Client(email='tester@example.com', password='secret', base_url='https://api.sandbox.dnsimple.com')
        client.dns_analytics.query(1, filter={'start_date': '2023-10-01', 'end_date': '2023-11-01'})
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.path_url,
                         '/v2/1/dns_analytics?start_date=2023-10-01&end_date=2023-11-01')

    @responses.activate
    def test_supports_sorting(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1/dns_analytics',
                                           fixture_name='dnsAnalytics/success'))
        client = Client(email='tester@example.com', password='secret', base_url='https://api.sandbox.dnsimple.com')
        client.dns_analytics.query(1, sort="date:desc,zone_name:desc")
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.path_url, '/v2/1/dns_analytics?sort=date%3Adesc%2Czone_name%3Adesc')

    @responses.activate
    def test_supports_grouping(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1/dns_analytics',
                                           fixture_name='dnsAnalytics/success'))
        client = Client(email='tester@example.com', password='secret', base_url='https://api.sandbox.dnsimple.com')
        client.dns_analytics.query(1, params={'groupings': "date,zone_name"})
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.path_url, '/v2/1/dns_analytics?groupings=date%2Czone_name')

    @responses.activate
    def test_supports_pagination(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1/dns_analytics',
                                           fixture_name='dnsAnalytics/success'))
        client = Client(email='tester@example.com', password='secret', base_url='https://api.sandbox.dnsimple.com')
        client.dns_analytics.query(1, page=33, per_page=200)
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.path_url, '/v2/1/dns_analytics?page=33&per_page=200')

        if __name__ == '__main__':
            unittest.main()
