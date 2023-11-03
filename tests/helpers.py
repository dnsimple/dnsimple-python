import os
import unittest

import responses

from dnsimple import Client


class DNSimpleMockResponse(responses.Response):
    def __init__(self, url='https://api.sandbox.dnsimple.com/v2', path='', method=None, fixture_name=None):
        url = f'{url}{path}'
        headers = {}
        dirname = os.path.abspath(os.path.dirname(__file__))
        fixture_path = os.path.join(dirname, 'fixtures/v2/api/{fixture_name}.http'.format(fixture_name=fixture_name))

        with open(fixture_path) as f:
            http_payload = f.read()
        split_payload = http_payload.splitlines()
        for header in split_payload:
            if not header:
                break
            if header.__contains__(':'):
                header_dic = header.split(':')
                headers[header_dic[0]] = header_dic[1]

        content = split_payload[len(split_payload) - 1]
        status_code = int(split_payload[0].split(' ')[1])
        super(DNSimpleMockResponse, self).__init__(method, url, body=content, headers=headers,
                                                   status=status_code)


class DNSimpleTest(unittest.TestCase):

    def setUp(self) -> None:
        self.client = Client(access_token='SomeMagicToken', sandbox=True)
        self.accounts = self.client.accounts
        self.billing = self.client.billing
        self.certificates = self.client.certificates
        self.contacts = self.client.contacts
        self.domains = self.client.domains
        self.identity = self.client.identity
        self.oauth = self.client.oauth
        self.registrar = self.client.registrar
        self.services = self.client.services
        self.templates = self.client.templates
        self.tlds = self.client.tlds
        self.vanity_name_servers = self.client.vanity_name_servers
        self.webhooks = self.client.webhooks
        self.zones = self.client.zones
