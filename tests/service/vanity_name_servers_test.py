import unittest

import responses

from dnsimple.struct import VanityNameServer
from tests.helpers import DNSimpleMockResponse, DNSimpleTest


class VanityNameServersTest(DNSimpleTest):
    @responses.activate
    def test_enable_vanity_name_servers(self):
        responses.add(DNSimpleMockResponse(method=responses.PUT,
                                           path='/1010/vanity/example.com',
                                           fixture_name='enableVanityNameServers/success'))
        vanity_name_servers = self.vanity_name_servers.enable_vanity_name_servers(1010, 'example.com').data

        self.assertEqual(4, len(vanity_name_servers))
        self.assertIsInstance(vanity_name_servers[0], VanityNameServer)

    @responses.activate
    def test_disable_vanity_name_servers(self):
        responses.add(DNSimpleMockResponse(method=responses.DELETE,
                                           path='/1010/vanity/example.com',
                                           fixture_name='disableVanityNameServers/success'))
        self.vanity_name_servers.disable_vanity_name_servers(1010, 'example.com')


if __name__ == '__main__':
    unittest.main()
