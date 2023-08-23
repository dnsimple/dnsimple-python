from dnsimple import DNSimpleException
from dnsimple.struct.zone import Zone
from tests.helpers import DNSimpleMockResponse
from tests.helpers import DNSimpleTest
import responses
import unittest


class ZonesTest(DNSimpleTest):
    @responses.activate
    def test_activate_zone(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.PUT,
                path="/1010/zones/example.com/activation",
                fixture_name="activateZoneService/success",
            )
        )
        zone = self.zones.activate_dns(1010, "example.com").data

        self.assertEqual(1, zone.id)
        self.assertEqual(1010, zone.account_id)
        self.assertEqual("example.com", zone.name)
        self.assertFalse(zone.reverse)
        self.assertEqual("2015-04-23T07:40:03Z", zone.created_at)
        self.assertEqual("2015-04-23T07:40:03Z", zone.updated_at)

    @responses.activate
    def test_deactivate_zone(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.DELETE,
                path="/1010/zones/example.com/activation",
                fixture_name="deactivateZoneService/success",
            )
        )
        zone = self.zones.deactivate_dns(1010, "example.com").data

        self.assertEqual(1, zone.id)
        self.assertEqual(1010, zone.account_id)
        self.assertEqual("example.com", zone.name)
        self.assertFalse(zone.reverse)
        self.assertEqual("2015-04-23T07:40:03Z", zone.created_at)
        self.assertEqual("2015-04-23T07:40:03Z", zone.updated_at)

    @responses.activate
    def test_list_zones(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.GET,
                path="/1010/zones",
                fixture_name="listZones/success",
            )
        )
        zones = self.zones.list_zones(1010).data
        self.assertEqual(2, len(zones))
        self.assertIsInstance(zones[0], Zone)

    @responses.activate
    def test_list_zones_supports_filtering(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.GET,
                path="/1010/zones?name_like=alpha.com",
                fixture_name="listZones/success",
            )
        )
        self.zones.list_zones(1010, filter={"name_like": "alpha.com"})

    @responses.activate
    def test_list_zones_supports_sorting(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.GET,
                path="/1010/zones?sort=id:asc,name:desc",
                fixture_name="listZones/success",
            )
        )
        self.zones.list_zones(1010, sort="id:asc,name:desc")

    @responses.activate
    def test_list_zones_supports_pagination(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.GET,
                path="/1010/zones?page=1&per_page=2",
                fixture_name="listZones/success",
            )
        )
        self.zones.list_zones(1010, page=1, per_page=2)

    @responses.activate
    def test_get_zone(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.GET,
                path="/1010/zones/example-alpha.com",
                fixture_name="getZone/success",
            )
        )
        zone = self.zones.get_zone(1010, "example-alpha.com").data

        self.assertEqual(1, zone.id)
        self.assertEqual(1010, zone.account_id)
        self.assertEqual("example-alpha.com", zone.name)
        self.assertFalse(zone.reverse)
        self.assertEqual("2015-04-23T07:40:03Z", zone.created_at)
        self.assertEqual("2015-04-23T07:40:03Z", zone.updated_at)

    @responses.activate
    def test_get_zone_file(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.GET,
                path="/1010/zones/example-alpha.com/file",
                fixture_name="getZoneFile/success",
            )
        )
        zone_file = self.zones.get_zone_file(1010, "example-alpha.com").data

        self.assertEqual(
            "$ORIGIN example.com.\n$TTL 1h\nexample.com. 3600 IN SOA ns1.dnsimple.com. "
            "admin.dnsimple.com. 1453132552 86400 7200 604800 300\nexample.com. 3600 IN NS "
            "ns1.dnsimple.com.\nexample.com. 3600 IN NS ns2.dnsimple.com.\nexample.com. 3600 IN NS "
            "ns3.dnsimple.com.\nexample.com. 3600 IN NS ns4.dnsimple.com.\n",
            zone_file.zone,
        )

    @responses.activate
    def test_check_zone_distribution(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.GET,
                path="/1010/zones/example-alpha.com/distribution",
                fixture_name="checkZoneDistribution/success",
            )
        )
        zone = self.zones.check_zone_distribution(1010, "example-alpha.com").data

        self.assertTrue(zone.distributed)

    @responses.activate
    def test_check_zone_distribution_failure(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.GET,
                path="/1010/zones/example-alpha.com/distribution",
                fixture_name="checkZoneDistribution/failure",
            )
        )
        zone = self.zones.check_zone_distribution(1010, "example-alpha.com").data

        self.assertFalse(zone.distributed)

    @responses.activate
    def test_check_zone_distribution_failure(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.GET,
                path="/1010/zones/example-alpha.com/distribution",
                fixture_name="checkZoneDistribution/error",
            )
        )
        try:
            self.zones.check_zone_distribution(1010, "example-alpha.com")
        except DNSimpleException as dnse:
            self.assertEqual("Could not query zone, connection time out", dnse.message)
            self.assertIsInstance(dnse, DNSimpleException)


if __name__ == "__main__":
    unittest.main()
