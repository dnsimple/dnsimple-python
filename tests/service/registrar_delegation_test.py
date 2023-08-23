from dnsimple.struct import VanityNameServer
from tests.helpers import DNSimpleMockResponse
from tests.helpers import DNSimpleTest
import responses
import unittest


class RegistrarDelegationTest(DNSimpleTest):
    @responses.activate
    def test_get_domain_delegation(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.GET,
                path="/1010/registrar/domains/example.com/delegation",
                fixture_name="getDomainDelegation/success",
            )
        )
        domain_delegation = self.registrar.get_domain_delegation(
            1010, "example.com"
        ).data

        self.assertListEqual(
            [
                "ns1.dnsimple.com",
                "ns2.dnsimple.com",
                "ns3.dnsimple.com",
                "ns4.dnsimple.com",
            ],
            domain_delegation,
        )

    @responses.activate
    def test_get_domain_delegation_empty(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.GET,
                path="/1010/registrar/domains/example.com/delegation",
                fixture_name="getDomainDelegation/success-empty",
            )
        )
        domain_delegation = self.registrar.get_domain_delegation(
            1010, "example.com"
        ).data

        self.assertListEqual([], domain_delegation)

    @responses.activate
    def test_change_domain_delegation(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.PUT,
                path="/1010/registrar/domains/example.com/delegation",
                fixture_name="changeDomainDelegation/success",
            )
        )
        domain_delegation = self.registrar.change_domain_delegation(
            1010,
            "example.com",
            [
                "ns1.dnsimple.com",
                "ns2.dnsimple.com",
                "ns3.dnsimple.com",
                "ns4.dnsimple.com",
            ],
        ).data

        self.assertListEqual(
            [
                "ns1.dnsimple.com",
                "ns2.dnsimple.com",
                "ns3.dnsimple.com",
                "ns4.dnsimple.com",
            ],
            domain_delegation,
        )

    @responses.activate
    def test_change_domain_delegation_to_vanity(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.PUT,
                path="/1010/registrar/domains/example.com/delegation/vanity",
                fixture_name="changeDomainDelegationToVanity/success",
            )
        )
        new_delegation = self.registrar.change_domain_delegation_to_vanity(
            1010, "example.com", ["ns1.example.com", "ns2.example.com"]
        ).data
        self.assertEqual(2, len(new_delegation))
        self.assertIsInstance(new_delegation[0], VanityNameServer)

    @responses.activate
    def test_chang_domain_delegation_from_vanity(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.DELETE,
                path="/1010/registrar/domains/example.com/delegation/vanity",
                fixture_name="changeDomainDelegationFromVanity/success",
            )
        )
        self.registrar.change_domain_delegation_from_vanity(1010, "example.com")


if __name__ == "__main__":
    unittest.main()
