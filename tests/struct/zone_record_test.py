import unittest

from dnsimple.struct.zone_record import ZoneRecordInput, ZoneRecordUpdateInput
from tests.helpers import DNSimpleTest, DNSimpleMockResponse

class ZoneRecordTest(DNSimpleTest):
    def test_zone_record_input_json_allows_empty_string_apex(self):
        zone_record_input = ZoneRecordInput('', 'A', '127.0.0.1')

        json = zone_record_input.to_json()
        self.assertEqual('{"type": "A", "content": "127.0.0.1", "name": ""}', json)

    def test_zone_record_input_json_rejects_none_apex(self):
        zone_record_input = ZoneRecordInput(None, 'A', '127.0.0.1')

        json = zone_record_input.to_json()
        self.assertEqual('{"type": "A", "content": "127.0.0.1"}', json)

    def test_zone_record_update_input_json_allows_empty_string_apex(self):
        zone_record_input = ZoneRecordUpdateInput('', '127.0.0.1', 3600)

        json = zone_record_input.to_json()
        self.assertEqual('{"content": "127.0.0.1", "ttl": 3600, "name": ""}', json)

    def test_zone_record_update_input_json_rejects_none_apex(self):
        zone_record_input = ZoneRecordUpdateInput(None, '127.0.0.1', 3600)

        json = zone_record_input.to_json()
        self.assertEqual('{"content": "127.0.0.1", "ttl": 3600}', json)

if __name__ == '__main__':
    unittest.main()
