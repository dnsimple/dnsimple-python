import unittest

import responses

from dnsimple import DNSimpleException
from dnsimple.struct.zone_record import ZoneRecord, ZoneRecordInput, ZoneRecordUpdateInput
from tests.helpers import DNSimpleTest, DNSimpleMockResponse


class ZoneRecordTest(DNSimpleTest):
    @responses.activate
    def test_list_zone_records(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/zones/example.com/records',
                                           fixture_name='listZoneRecords/success'))
        zone_records = self.zones.list_records(1010, 'example.com').data

        self.assertEqual(5, len(zone_records))
        self.assertIsInstance(zone_records[0], ZoneRecord)

    @responses.activate
    def test_list_records_supports_filtering(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/zones/example.com/records?type=SOA',
                                           fixture_name='listZoneRecords/success'))
        self.zones.list_records(1010, 'example.com', filter={'type': 'SOA'})

    @responses.activate
    def test_list_records_supports_sorting(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/zones/example.com/records?sort=content:asc',
                                           fixture_name='listZoneRecords/success'))
        self.zones.list_records(1010, 'example.com', sort='content:asc')

    @responses.activate
    def test_list_records_supports_pagination(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/zones/example.com/records?page=1&per_page=5',
                                           fixture_name='listZoneRecords/success'))
        self.zones.list_records(1010, 'example.com', page=1, per_page=5)

    @responses.activate
    def test_create_record(self):
        responses.add(DNSimpleMockResponse(method=responses.POST,
                                           path='/1010/zones/example.com/records',
                                           fixture_name='createZoneRecord/created'))
        record = self.zones.create_record(1010, 'example.com', ZoneRecordInput('www', 'A', '127.0.0.1')).data
        self.assertEqual('www', record.name)

    @responses.activate
    def test_create_apex_record(self):
        responses.add(DNSimpleMockResponse(method=responses.POST,
                                           path='/1010/zones/example.com/records',
                                           fixture_name='createZoneRecord/created-apex'))
        record = self.zones.create_record(1010, 'example.com', ZoneRecordInput('', 'A', '127.0.0.1')).data
        self.assertEqual('', record.name)

    @responses.activate
    def test_get_record(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/zones/example.com/records/5',
                                           fixture_name="getZoneRecord/success"))
        record = self.zones.get_record(1010, 'example.com', 5).data

        self.assertEqual(5, record.id)
        self.assertEqual('example.com', record.zone_id)
        self.assertIsNone(record.parent_id)
        self.assertEqual('', record.name)
        self.assertEqual('mxa.example.com', record.content)
        self.assertEqual(600, record.ttl)
        self.assertEqual(10, record.priority)
        self.assertEqual('MX', record.type)
        self.assertListEqual(["SV1", "IAD"], record.regions)
        self.assertFalse(record.system_record)
        self.assertEqual('2016-10-05T09:51:35Z', record.created_at)
        self.assertEqual('2016-10-05T09:51:35Z', record.updated_at)

    @responses.activate
    def test_update_record(self):
        responses.add(DNSimpleMockResponse(method=responses.PATCH,
                                           path='/1010/zones/example.com/records/5',
                                           fixture_name='updateZoneRecord/success'))
        record = self.zones.update_record(1010, 'example.com', 5, ZoneRecordUpdateInput(name='', content='mxb.example.com')).data

        self.assertEqual('', record.name)
        self.assertEqual('mxb.example.com', record.content)

    @responses.activate
    def test_delete_record(self):
        responses.add(DNSimpleMockResponse(method=responses.DELETE,
                                           path='/1010/zones/example.com/records/5',
                                           fixture_name='deleteZoneRecord/success'))
        self.zones.delete_record(1010, 'example.com', 5)

    @responses.activate
    def test_check_record_distribution(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/zones/example.com/records/5/distribution',
                                           fixture_name="checkZoneRecordDistribution/success"))
        distribution = self.zones.check_zone_record_distribution(1010, 'example.com', 5).data

        self.assertTrue(distribution.distributed)

    @responses.activate
    def test_check_record_distribution_failure(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/zones/example.com/records/5/distribution',
                                           fixture_name="checkZoneRecordDistribution/failure"))
        distribution = self.zones.check_zone_record_distribution(1010, 'example.com', 5).data

        self.assertFalse(distribution.distributed)

    @responses.activate
    def test_check_record_distribution_error(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/zones/example.com/records/5/distribution',
                                           fixture_name="checkZoneRecordDistribution/error"))
        try:
            self.zones.check_zone_record_distribution(1010, 'example.com', 5)
        except DNSimpleException as dnse:
            self.assertEqual('Could not query zone, connection time out', dnse.message)
            self.assertIsInstance(dnse, DNSimpleException)



if __name__ == '__main__':
    unittest.main()
