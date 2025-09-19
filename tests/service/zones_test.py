import unittest

import responses

from dnsimple import DNSimpleException
from dnsimple.struct.zone import Zone
from dnsimple.struct.batch_change_zone_records import (
    BatchChangeZoneRecordsInput,
    BatchChangeZoneRecordsUpdateInput,
    BatchChangeZoneRecordsDeleteInput,
    BatchChangeZoneRecordsResponse
)
from dnsimple.struct.zone_record import ZoneRecordInput
from dnsimple.struct.zone_record import ZoneRecord
from tests.helpers import DNSimpleTest, DNSimpleMockResponse


class ZonesTest(DNSimpleTest):
    @responses.activate
    def test_activate_zone(self):
        responses.add(DNSimpleMockResponse(method=responses.PUT,
                                           path='/1010/zones/example.com/activation',
                                           fixture_name='activateZoneService/success'))
        zone = self.zones.activate_dns(1010, 'example.com').data

        self.assertEqual(1, zone.id)
        self.assertEqual(1010, zone.account_id)
        self.assertEqual('example.com', zone.name)
        self.assertFalse(zone.reverse)
        self.assertTrue(zone.active)
        self.assertEqual('2022-09-28T04:45:24Z', zone.created_at)
        self.assertEqual('2023-07-06T11:19:48Z', zone.updated_at)

    @responses.activate
    def test_deactivate_zone(self):
        responses.add(DNSimpleMockResponse(method=responses.DELETE,
                                           path='/1010/zones/example.com/activation',
                                           fixture_name='deactivateZoneService/success'))
        zone = self.zones.deactivate_dns(1010, 'example.com').data

        self.assertEqual(1, zone.id)
        self.assertEqual(1010, zone.account_id)
        self.assertEqual('example.com', zone.name)
        self.assertFalse(zone.reverse)
        self.assertFalse(zone.active)
        self.assertEqual('2022-09-28T04:45:24Z', zone.created_at)
        self.assertEqual('2023-08-08T04:19:52Z', zone.updated_at)

    @responses.activate
    def test_list_zones(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/zones',
                                           fixture_name='listZones/success'))
        zones = self.zones.list_zones(1010).data
        self.assertEqual(2, len(zones))
        self.assertIsInstance(zones[0], Zone)

    @responses.activate
    def test_list_zones_supports_filtering(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/zones?name_like=alpha.com',
                                           fixture_name='listZones/success'))
        self.zones.list_zones(1010, filter={'name_like': 'alpha.com'})

    @responses.activate
    def test_list_zones_supports_sorting(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/zones?sort=id:asc,name:desc',
                                           fixture_name='listZones/success'))
        self.zones.list_zones(1010, sort='id:asc,name:desc')

    @responses.activate
    def test_list_zones_supports_pagination(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/zones?page=1&per_page=2',
                                           fixture_name='listZones/success'))
        self.zones.list_zones(1010, page=1, per_page=2)

    @responses.activate
    def test_get_zone(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/zones/example-alpha.com',
                                           fixture_name='getZone/success'))
        zone = self.zones.get_zone(1010, 'example-alpha.com').data

        self.assertEqual(1, zone.id)
        self.assertEqual(1010, zone.account_id)
        self.assertEqual('example-alpha.com', zone.name)
        self.assertFalse(zone.reverse)
        self.assertFalse(zone.secondary)
        self.assertEqual(None, zone.last_transferred_at)
        self.assertTrue(zone.active)
        self.assertEqual('2015-04-23T07:40:03Z', zone.created_at)
        self.assertEqual('2015-04-23T07:40:03Z', zone.updated_at)

    @responses.activate
    def test_get_zone_file(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/zones/example-alpha.com/file',
                                           fixture_name='getZoneFile/success'))
        zone_file = self.zones.get_zone_file(1010, 'example-alpha.com').data

        self.assertEqual('$ORIGIN example.com.\n$TTL 1h\nexample.com. 3600 IN SOA ns1.dnsimple.com. '
                         'admin.dnsimple.com. 1453132552 86400 7200 604800 300\nexample.com. 3600 IN NS '
                         'ns1.dnsimple.com.\nexample.com. 3600 IN NS ns2.dnsimple.com.\nexample.com. 3600 IN NS '
                         'ns3.dnsimple.com.\nexample.com. 3600 IN NS ns4.dnsimple.com.\n', zone_file.zone)

    @responses.activate
    def test_check_zone_distribution(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/zones/example-alpha.com/distribution',
                                           fixture_name='checkZoneDistribution/success'))
        zone = self.zones.check_zone_distribution(1010, 'example-alpha.com').data

        self.assertTrue(zone.distributed)

    @responses.activate
    def test_check_zone_distribution_failure(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/zones/example-alpha.com/distribution',
                                           fixture_name='checkZoneDistribution/failure'))
        zone = self.zones.check_zone_distribution(1010, 'example-alpha.com').data

        self.assertFalse(zone.distributed)

    @responses.activate
    def test_check_zone_distribution_failure(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/zones/example-alpha.com/distribution',
                                           fixture_name='checkZoneDistribution/error'))
        try:
            self.zones.check_zone_distribution(1010, 'example-alpha.com')
        except DNSimpleException as dnse:
            self.assertEqual('Could not query zone, connection time out', dnse.message)
            self.assertIsInstance(dnse, DNSimpleException)

    @responses.activate
    def test_batch_change_records_success(self):
        responses.add(DNSimpleMockResponse(method=responses.POST,
                                           path='/1010/zones/example.com/batch',
                                           fixture_name='batchChangeZoneRecords/success'))

        batch_change = BatchChangeZoneRecordsInput(
            creates=[
                ZoneRecordInput('ab', 'A', '3.2.3.4'),
                ZoneRecordInput('ab', 'A', '4.2.3.4')
            ],
            updates=[
                BatchChangeZoneRecordsUpdateInput(67622534, content='3.2.3.40'),
                BatchChangeZoneRecordsUpdateInput(67622537, content='5.2.3.40')
            ],
            deletes=[
                BatchChangeZoneRecordsDeleteInput(67622509),
                BatchChangeZoneRecordsDeleteInput(67622527)
            ]
        )

        response = self.zones.batch_change_records(1010, 'example.com', batch_change)
        result = response.data

        self.assertIsInstance(result, BatchChangeZoneRecordsResponse)

        self.assertEqual(2, len(result.creates))
        self.assertIsInstance(result.creates[0], ZoneRecord)
        self.assertEqual(67623409, result.creates[0].id)
        self.assertEqual('ab', result.creates[0].name)
        self.assertEqual('3.2.3.4', result.creates[0].content)
        self.assertEqual('A', result.creates[0].type)

        self.assertEqual(2, len(result.updates))
        self.assertIsInstance(result.updates[0], ZoneRecord)
        self.assertEqual(67622534, result.updates[0].id)
        self.assertEqual('3.2.3.40', result.updates[0].content)

        self.assertEqual(2, len(result.deletes))
        self.assertEqual(67622509, result.deletes[0].id)
        self.assertEqual(67622527, result.deletes[1].id)

    @responses.activate
    def test_batch_change_records_create_validation_failed(self):
        responses.add(DNSimpleMockResponse(method=responses.POST,
                                           path='/1010/zones/example.com/batch',
                                           fixture_name='batchChangeZoneRecords/error_400_create_validation_failed'))

        batch_change = BatchChangeZoneRecordsInput(
            creates=[
                ZoneRecordInput('test', 'SPF', 'v=spf1 -all')
            ]
        )

        try:
            self.zones.batch_change_records(1010, 'example.com', batch_change)
        except DNSimpleException as dnse:
            self.assertEqual('Validation failed', dnse.message)
            self.assertIsInstance(dnse, DNSimpleException)
            self.assertEqual('The SPF record type has been discontinued', dnse.attribute_errors['creates'][0]['message'])

    @responses.activate
    def test_batch_change_records_update_validation_failed(self):
        responses.add(DNSimpleMockResponse(method=responses.POST,
                                           path='/1010/zones/example.com/batch',
                                           fixture_name='batchChangeZoneRecords/error_400_update_validation_failed'))

        batch_change = BatchChangeZoneRecordsInput(
            updates=[
                BatchChangeZoneRecordsUpdateInput(99999999, content='1.2.3.4')
            ]
        )

        try:
            self.zones.batch_change_records(1010, 'example.com', batch_change)
        except DNSimpleException as dnse:
            self.assertEqual('Validation failed', dnse.message)
            self.assertIsInstance(dnse, DNSimpleException)
            self.assertEqual('Record not found ID=99999999', dnse.attribute_errors['updates'][0]['message'])

    @responses.activate
    def test_batch_change_records_delete_validation_failed(self):
        responses.add(DNSimpleMockResponse(method=responses.POST,
                                           path='/1010/zones/example.com/batch',
                                           fixture_name='batchChangeZoneRecords/error_400_delete_validation_failed'))

        batch_change = BatchChangeZoneRecordsInput(
            deletes=[
                BatchChangeZoneRecordsDeleteInput(67622509)
            ]
        )

        try:
            self.zones.batch_change_records(1010, 'example.com', batch_change)
        except DNSimpleException as dnse:
            self.assertEqual('Validation failed', dnse.message)
            self.assertIsInstance(dnse, DNSimpleException)
            self.assertEqual('Record not found ID=67622509', dnse.attribute_errors['deletes'][0]['message'])


if __name__ == '__main__':
    unittest.main()
