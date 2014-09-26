__author__ = 'Chris Morgan'

import unittest
from dnsimple import DNSimple, DNSimpleException


class RecordsTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dns = DNSimple(sandbox=True)
        domains = cls.dns.domains()

        for domain in domains:
            cls.dns.delete(domain['domain']['name'])

        new_domain = cls.dns.add_domain('test.test')
        cls.success_domain_id = new_domain['domain']['id']
        cls.success_domain_name = new_domain['domain']['name']

        new_record_data = {
            'record_type': 'CNAME',
            'name': 'test',
            'content': 'test.test'
        }
        new_record = cls.dns.add_record(new_domain['domain']['id'], new_record_data)
        cls.success_record_id = new_record['record']['id']
        cls.success_record_name = new_record['record']['name']

        record_to_delete_data = {
            'record_type': 'CNAME',
            'name': 'deletebyid',
            'content': 'test.test'
        }

        record_to_delete = cls.dns.add_record(cls.success_domain_id, record_to_delete_data)
        cls.record_to_delete_id = record_to_delete['record']['id']

        cls.failure_id = '0'
        cls.failure_name = 'i.dont.own.this.domain'

    def test_get_records_by(self):
        self.assertTrue(type(self.dns.records(self.success_domain_id)) is list)

    def test_get_record(self):
        domain = self.dns.record(self.success_domain_id, self.success_record_id)
        self.assertTrue('record' in domain)

    def test_add_record(self):
        data = {
            'record_type': 'CNAME',
            'name': 'testaddrecord',
            'content': 'test.test'
        }
        self.assertTrue('record' in self.dns.add_record(self.success_domain_id, data))

    def test_add_record_failure(self):
        data = {
            'record_type': 'CNAME',
            'name': 'test',
            'content': 'test.test'
        }
        self.assertRaises(DNSimpleException, self.dns.add_record, self.success_domain_id, data)

    def test_delete_record(self):
        self.assertFalse(self.dns.delete_record(self.success_domain_id, self.record_to_delete_id))

    def test_delete_record_failure(self):
        self.assertRaises(DNSimpleException, self.dns.delete_record, self.success_domain_id, self.failure_id)


if __name__ == '__main__':
    unittest.main()
