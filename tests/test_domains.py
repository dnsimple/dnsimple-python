__author__ = 'Chris Morgan'

import unittest
from dnsimple import DNSimple, DNSimpleException


class DomainsTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dns = DNSimple(sandbox=True)
        domains = cls.dns.domains()

        for domain in domains:
            cls.dns.delete(domain['domain']['name'])

        new_domain = cls.dns.add_domain('test.test')
        cls.success_domain_id = new_domain['domain']['id']
        cls.success_domain_name = new_domain['domain']['name']

        domain_to_delete_by_id = cls.dns.add_domain('deletebyid.test')
        cls.domain_to_delete_id = domain_to_delete_by_id['domain']['id']

        domain_to_delete_by_name = cls.dns.add_domain('deletebyname.test')
        cls.domain_to_delete_name = domain_to_delete_by_name['domain']['name']

        cls.failure_domain_id = '0'
        cls.failure_domain_name = 'i.dont.own.this.domain'

    def test_check_record(self):
        self.assertTrue('status' in self.dns.check(self.success_domain_name))

    def test_get_records(self):
        self.assertTrue(type(self.dns.domains()) is list)

    def test_get_domain_by_id(self):
        domain = self.dns.domain(self.success_domain_id)
        self.assertTrue('domain' in domain)

    def test_get_domain_by_name(self):
        domain = self.dns.domain(self.success_domain_name)
        self.assertTrue('domain' in domain)

    def test_get_domain_by_name_failure(self):
        self.assertRaises(DNSimpleException, self.dns.domain, self.failure_domain_name)

    def test_add_domain(self):
        self.assertTrue('domain' in self.dns.add_domain('add.test'))

    def test_add_domain_failure(self):
        self.assertRaises(DNSimpleException, self.dns.add_domain, self.success_domain_name)

    def test_delete_domain_by_name(self):
        self.assertFalse(self.dns.delete(self.domain_to_delete_name))

    def test_delete_domain_by_id(self):
        self.assertFalse(self.dns.delete(self.domain_to_delete_id))

    def test_delete_domain_by_name_failure(self):
        self.assertRaises(DNSimpleException, self.dns.delete, self.failure_domain_name)

    def test_delete_domain_by_id_failure(self):
        self.assertRaises(DNSimpleException, self.dns.delete, self.failure_domain_id)

if __name__ == '__main__':
    unittest.main()
