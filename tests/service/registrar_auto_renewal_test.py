import unittest

import responses

from tests.helpers import DNSimpleMockResponse, DNSimpleTest


class RegistrarAutoRenewalTest(DNSimpleTest):
    @responses.activate
    def test_enable_domain_auto_renewal(self):
        responses.add(DNSimpleMockResponse(method=responses.PUT,
                                           path='/1010/registrar/domains/example.com/auto_renewal',
                                           fixture_name='enableDomainAutoRenewal/success'))
        self.registrar.enable_domain_auto_renewal(1010, 'example.com')

    @responses.activate
    def test_disable_domain_auto_renewal(self):
        responses.add(DNSimpleMockResponse(method=responses.DELETE,
                                           path='/1010/registrar/domains/example.com/auto_renewal',
                                           fixture_name='disableDomainAutoRenewal/success'))
        self.registrar.disable_domain_auto_renewal(1010, 'example.com')
        

if __name__ == '__main__':
    unittest.main()