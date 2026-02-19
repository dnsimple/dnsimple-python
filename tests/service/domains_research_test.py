import unittest

import responses

from dnsimple.response import Response
from dnsimple.struct import DomainResearchStatus
from tests.helpers import DNSimpleTest, DNSimpleMockResponse


class DomainsResearchTest(DNSimpleTest):
    @responses.activate
    def test_domain_research_status(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/domains/research/status?domain=taken.com',
                                           fixture_name='getDomainsResearchStatus/success-unavailable'))
        research = self.domains.domain_research_status(1010, 'taken.com').data

        self.assertIsInstance(research, DomainResearchStatus)
        self.assertEqual('25dd77cb-2f71-48b9-b6be-1dacd2881418', research.request_id)
        self.assertEqual('taken.com', research.domain)
        self.assertEqual('unavailable', research.availability)
        self.assertEqual([], research.errors)


if __name__ == '__main__':
    unittest.main()
