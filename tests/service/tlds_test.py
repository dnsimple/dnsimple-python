import unittest

import responses

from dnsimple.response import Pagination
from dnsimple.struct import Tld, TldExtendedAttribute, TldExtendedAttributeOption
from tests.helpers import DNSimpleMockResponse, DNSimpleTest


class TldsTest(DNSimpleTest):
    @responses.activate
    def test_list_tlds(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/tlds',
                                           fixture_name='listTlds/success'))
        tlds = self.tlds.list_tlds().data

        self.assertEqual(2, len(tlds))
        self.assertIsInstance(tlds[0], Tld)

    @responses.activate
    def test_list_tlds_supports_pagination(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/tlds',
                                           fixture_name='listTlds/success'))
        response = self.tlds.list_tlds()

        self.assertIsInstance(response.pagination, Pagination)

    @responses.activate
    def test_list_tlds_supports_sorting(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/tlds?sort=tld:asc',
                                           fixture_name='listTlds/success'))
        self.tlds.list_tlds(sort='tld:asc')

    @responses.activate
    def test_get_tld(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/tlds/com',
                                           fixture_name='getTld/success'))
        tld = self.tlds.get_tld('com').data

        self.assertEqual('com', tld.tld)
        self.assertEqual(1, tld.tld_type)
        self.assertTrue(tld.whois_privacy)
        self.assertFalse(tld.auto_renew_only)
        self.assertTrue(tld.idn)
        self.assertEqual(1, tld.minimum_registration)
        self.assertTrue(tld.registration_enabled)
        self.assertTrue(tld.renewal_enabled)
        self.assertTrue(tld.transfer_enabled)
        self.assertEqual(tld.dnssec_interface_type, 'ds')

    @responses.activate
    def test_get_tld_extended_attributes(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/tlds/com/extended_attributes',
                                           fixture_name='getTldExtendedAttributes/success'))
        tld_attributes = self.tlds.get_tld_extended_attributes('com').data

        self.assertEqual(4, len(tld_attributes))
        self.assertIsInstance(tld_attributes[0], TldExtendedAttribute)
        self.assertIsInstance(tld_attributes[0].options[0], TldExtendedAttributeOption)

    @responses.activate
    def test_get_tld_extended_attributes_no_attributes(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/tlds/com/extended_attributes',
                                           fixture_name='getTldExtendedAttributes/success-noattributes'))
        tld_attributes = self.tlds.get_tld_extended_attributes('com').data

        self.assertListEqual([], tld_attributes)


if __name__ == '__main__':
    unittest.main()
