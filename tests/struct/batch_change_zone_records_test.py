import unittest
import json

from dnsimple.struct.batch_change_zone_records import (
    BatchChangeZoneRecordsCreateInput,
    BatchChangeZoneRecordsUpdateInput,
    BatchChangeZoneRecordsDeleteInput,
    BatchChangeZoneRecordsInput
)
from tests.helpers import DNSimpleTest


class BatchChangeZoneRecordsTest(DNSimpleTest):
    def test_batch_change_zone_records_update_input_json_allows_empty_string_apex(self):
        update_input = BatchChangeZoneRecordsUpdateInput(12345, name='', content='127.0.0.1', ttl=3600)

        json = update_input.to_json()
        self.assertEqual('{"id": 12345, "name": "", "content": "127.0.0.1", "ttl": 3600}', json)

    def test_batch_change_zone_records_update_input_json_rejects_none_apex(self):
        update_input = BatchChangeZoneRecordsUpdateInput(12345, name=None, content='127.0.0.1', ttl=3600)

        json = update_input.to_json()
        self.assertEqual('{"id": 12345, "content": "127.0.0.1", "ttl": 3600}', json)

    def test_batch_change_zone_records_update_input_json_with_all_fields(self):
        update_input = BatchChangeZoneRecordsUpdateInput(12345, name='', content='10 mail.example.com', ttl=7200, priority=5, regions=['us-east', 'us-west'])

        json = update_input.to_json()
        self.assertEqual('{"id": 12345, "name": "", "content": "10 mail.example.com", "ttl": 7200, "priority": 5, "regions": ["us-east", "us-west"]}', json)

    def test_batch_change_zone_records_input_creates_only(self):
        creates = [
            BatchChangeZoneRecordsCreateInput('www', 'A', '127.0.0.1'),
            BatchChangeZoneRecordsCreateInput('', 'A', '127.0.0.2')
        ]
        batch_input = BatchChangeZoneRecordsInput(creates=creates)

        json_str = batch_input.to_json()
        parsed = json.loads(json_str)

        self.assertIn('creates', parsed)
        self.assertEqual(2, len(parsed['creates']))
        self.assertEqual('www', parsed['creates'][0]['name'])
        self.assertEqual('', parsed['creates'][1]['name'])
        self.assertNotIn('updates', parsed)
        self.assertNotIn('deletes', parsed)

    def test_batch_change_zone_records_input_updates_only(self):
        updates = [
            BatchChangeZoneRecordsUpdateInput(12345, content='127.0.0.1'),
            BatchChangeZoneRecordsUpdateInput(12346, name='', content='127.0.0.2')
        ]
        batch_input = BatchChangeZoneRecordsInput(updates=updates)

        json_str = batch_input.to_json()
        parsed = json.loads(json_str)

        self.assertIn('updates', parsed)
        self.assertEqual(2, len(parsed['updates']))
        # Test that the name field is omitted
        self.assertNotIn('name', parsed['updates'][0])
        self.assertEqual('127.0.0.1', parsed['updates'][0]['content'])
        # Test that name is empty
        self.assertIn('name', parsed['updates'][1])
        self.assertEqual('', parsed['updates'][1]['name'])
        self.assertNotIn('creates', parsed)
        self.assertNotIn('deletes', parsed)

    def test_batch_change_zone_records_input_deletes_only(self):
        deletes = [
            BatchChangeZoneRecordsDeleteInput(12345),
            BatchChangeZoneRecordsDeleteInput(12346)
        ]
        batch_input = BatchChangeZoneRecordsInput(deletes=deletes)

        json_str = batch_input.to_json()
        parsed = json.loads(json_str)

        self.assertIn('deletes', parsed)
        self.assertEqual(2, len(parsed['deletes']))
        self.assertEqual(12345, parsed['deletes'][0]['id'])
        self.assertEqual(12346, parsed['deletes'][1]['id'])
        self.assertNotIn('creates', parsed)
        self.assertNotIn('updates', parsed)

    def test_batch_change_zone_records_input_combined_operations(self):
        creates = [BatchChangeZoneRecordsCreateInput('ftp', 'A', '127.0.0.1')]
        updates = [BatchChangeZoneRecordsUpdateInput(12345, content='127.0.0.2')]
        deletes = [BatchChangeZoneRecordsDeleteInput(12346)]

        batch_input = BatchChangeZoneRecordsInput(creates=creates, updates=updates, deletes=deletes)

        json_str = batch_input.to_json()
        parsed = json.loads(json_str)

        self.assertIn('creates', parsed)
        self.assertIn('updates', parsed)
        self.assertIn('deletes', parsed)

        self.assertEqual(1, len(parsed['creates']))
        self.assertEqual('ftp', parsed['creates'][0]['name'])

        self.assertEqual(1, len(parsed['updates']))
        self.assertNotIn('name', parsed['updates'][0])
        self.assertEqual(1, len(parsed['deletes']))
        self.assertEqual(12346, parsed['deletes'][0]['id'])

    def test_batch_change_zone_records_input_no_null_values_in_nested_objects(self):
        creates = [
            BatchChangeZoneRecordsCreateInput('www', 'A', '127.0.0.1'),
        ]
        updates = [
            BatchChangeZoneRecordsUpdateInput(12345, content='127.0.0.2'),
        ]

        batch_input = BatchChangeZoneRecordsInput(creates=creates, updates=updates)
        json_str = batch_input.to_json()

        self.assertNotIn('null', json_str)

        parsed = json.loads(json_str)

        create = parsed['creates'][0]
        for key, value in create.items():
            self.assertIsNotNone(value, f"Create field '{key}' should not be None")

        update = parsed['updates'][0]
        for key, value in update.items():
            self.assertIsNotNone(value, f"Update field '{key}' should not be None")

        self.assertNotIn('name', update)

    def test_batch_change_zone_records_input_apex_record_name_preservation(self):
        updates = [
            BatchChangeZoneRecordsUpdateInput(12345, name='', content='127.0.0.1'),
            BatchChangeZoneRecordsUpdateInput(12346, content='127.0.0.2'),
            BatchChangeZoneRecordsUpdateInput(12347, name='mail', content='127.0.0.3'),
        ]

        batch_input = BatchChangeZoneRecordsInput(updates=updates)
        json_str = batch_input.to_json()
        parsed = json.loads(json_str)

        updates_data = parsed['updates']

        self.assertIn('name', updates_data[0])
        self.assertEqual('', updates_data[0]['name'])
        self.assertNotIn('name', updates_data[1])
        self.assertIn('name', updates_data[2])
        self.assertEqual('mail', updates_data[2]['name'])

if __name__ == '__main__':
    unittest.main()
