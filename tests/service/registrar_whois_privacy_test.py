import unittest

import responses

from dnsimple.struct import WhoisPrivacy
from tests.helpers import DNSimpleMockResponse, DNSimpleTest


class RegistrarWhoisPrivacyTest(DNSimpleTest):
    @responses.activate
    def test_enable_whois_privacy(self):
        responses.add(DNSimpleMockResponse(method=responses.PUT,
                                           path='/1010/registrar/domains/example.com/whois_privacy',
                                           fixture_name='enableWhoisPrivacy/success'))
        whois_privacy = self.registrar.enable_whois_privacy(1010, 'example.com').data

        self.assertTrue(whois_privacy.enabled)

    @responses.activate
    def test_enable_whois_privacy_newly_purchased(self):
        responses.add(DNSimpleMockResponse(method=responses.PUT,
                                           path='/1010/registrar/domains/example.com/whois_privacy',
                                           fixture_name='enableWhoisPrivacy/created'))
        whois_privacy = self.registrar.enable_whois_privacy(1010, 'example.com').data

        self.assertIsNone(whois_privacy.enabled)
        self.assertIsNone(whois_privacy.expires_on)

    @responses.activate
    def test_disable_whois_privacy(self):
        responses.add(DNSimpleMockResponse(method=responses.DELETE,
                                           path='/1010/registrar/domains/example.com/whois_privacy',
                                           fixture_name='disableWhoisPrivacy/success'))
        whois_privacy = self.registrar.disable_whois_privacy(1010, 'example.com').data

        self.assertFalse(whois_privacy.enabled)


if __name__ == '__main__':
    unittest.main()
