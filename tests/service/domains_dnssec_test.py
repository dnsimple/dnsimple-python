import unittest

import responses

from dnsimple import DNSimpleException
from tests.helpers import DNSimpleMockResponse, DNSimpleTest


class DomainDNSSECTest(DNSimpleTest):
    @responses.activate
    def test_enable_dnssec(self):
        responses.add(DNSimpleMockResponse(method=responses.POST,
                                           path='/1010/domains/1/dnssec',
                                           fixture_name='enableDnssec/success'))
        dnssec = self.domains.enable_dnssec(1010, 1).data
        self.assertTrue(dnssec.enabled)

    @responses.activate
    def test_disable_dnssec(self):
        responses.add(DNSimpleMockResponse(method=responses.DELETE,
                                           path='/1010/domains/1/dnssec',
                                           fixture_name='disableDnssec/success'))

        self.domains.disable_dnssec(1010, 1)

    @responses.activate
    def test_disable_dnssec_not_enabled(self):
        responses.add(DNSimpleMockResponse(method=responses.DELETE,
                                           path='/1010/domains/1/dnssec',
                                           fixture_name='disableDnssec/not-enabled'))
        try:
            self.domains.disable_dnssec(1010, 1)
        except DNSimpleException as dnse:
            self.assertEqual(dnse.message, 'DNSSEC cannot be disabled because it is not enabled')

    @responses.activate
    def test_get_dnssec(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/domains/1/dnssec',
                                           fixture_name='getDnssec/success'))
        dnssec = self.domains.get_dnssec(1010, 1).data

        self.assertTrue(dnssec.enabled)


if __name__ == '__main__':
    unittest.main()
