__author__ = 'Chris Morgan'

import unittest
from dnsimple import DNSimple, DNSimpleException


class DomainsTestCase(unittest.TestCase):

    def setUp(self):
        self.test_success_domain_id = '940'
        self.test_success_domain_name = 'test.test'
        self.test_failure_domain_id = '0'
        self.test_failure_domain_name = 'i.dont.own.this.domain'
        self.dns = DNSimple(sandbox=True)

    def test_get_domains(self):
        self.assertTrue(type(self.dns.domains()) is list)

    def test_get_domain_by_id(self):
        domain = self.dns.domain('940')
        self.assertTrue('domain' in domain)

    def test_get_domain_by_name(self):
        domain = self.dns.domain(self.test_success_domain_name)
        self.assertTrue('domain' in domain)

    def test_get_domain_by_name_failure(self):
        self.assertRaises(DNSimpleException, self.dns.domain, self.test_failure_domain_name)

if __name__ == '__main__':
    unittest.main()
