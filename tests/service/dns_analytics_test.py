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


if __name__ == '__main__':
    unittest.main()
