import unittest

import responses

from dnsimple.response import Response
from dnsimple.struct import DomainResearchStatus
from tests.helpers import DNSimpleTest, DNSimpleMockResponse


class DomainsResearchTest(DNSimpleTest):
    @responses.activate
    def test_domain_research_status(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/domains/research/status?domain=example.com',
                                           fixture_name='domainResearchStatus/success'))
        research = self.domains.domain_research_status(1010, 'example.com').data

        self.assertIsInstance(research, DomainResearchStatus)
        self.assertEqual('f453dabc-a27e-4bf1-a93e-f263577ffaae', research.request_id)
        self.assertEqual('example.com', research.domain)
        self.assertEqual('unavailable', research.availability)
        self.assertEqual([], research.errors)


if __name__ == '__main__':
    unittest.main()
