__author__ = 'Chris Morgan'

import unittest
from dnsimple import DNSimple, DNSimpleException


class AuthTestCase(unittest.TestCase):

    def test_username_and_password_auth(self):
        dns = DNSimple(username='chris.morgan@youngshand.com', password='dnsimple-python', sandbox=True)
        self.assertTrue(type(dns.domains()) is list)

    def test_email_and_api_token_auth(self):
        dns = DNSimple(email='chris.morgan@youngshand.com', api_token='L0lkPizHnqVrsIyViLpB', sandbox=True)
        self.assertTrue(type(dns.domains()) is list)

    def test_domain_token_auth(self):
        dns = DNSimple(api_token='DOMAIN_TOKEN', single_domain=True, sandbox=True)
        with self.assertRaises(DNSimpleException):
            self.assertTrue(type(dns.domains()) is list)
        # FIXME: Needs proper credentials
        self.assertTrue(type(dns.records('DOMAIN')) is list)

    def test_config_auth(self):
        dns = DNSimple(sandbox=True)
        self.assertTrue(type(dns.domains()) is list)


if __name__ == '__main__':
    unittest.main()
