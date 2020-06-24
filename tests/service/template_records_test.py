import unittest

import responses

from dnsimple.struct import TemplateRecord
from tests.helpers import DNSimpleMockResponse, DNSimpleTest


class TemplateRecordsTest(DNSimpleTest):
    @responses.activate
    def test_list_template_records(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/templates/296/records',
                                           fixture_name='listTemplateRecords/success'))
        records = self.templates.list_template_records(1010, 296).data

        self.assertEqual(2, len(records))
        self.assertIsInstance(records[0], TemplateRecord)

    @responses.activate
    def test_list_template_records_supports_pagination(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/templates/296/records?page=1&per_page=2',
                                           fixture_name='listTemplateRecords/success'))
        self.templates.list_template_records(1010, 296, page=1, per_page=2)

    @responses.activate
    def test_list_template_records_supports_sorting(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/templates/296/records?sort=id:asc,name:desc,content:asc,'
                                                'type:desc',
                                           fixture_name='listTemplateRecords/success'))
        self.templates.list_template_records(1010, 296, sort='id:asc,name:desc,content:asc,type:desc')

    @responses.activate
    def test_create_template_record(self):
        responses.add(DNSimpleMockResponse(method=responses.POST,
                                           path='/1010/templates/268/records',
                                           fixture_name='createTemplateRecord/created'))
        record = TemplateRecord.new('', 'MX', 'mx.example.com', ttl=600, priority=10)

        new_record = self.templates.create_template_record(1010, 268, record).data

        self.assertEqual(record.name, new_record.name)
        self.assertEqual(record.type, new_record.type)
        self.assertEqual(record.content, new_record.content)
        self.assertEqual(record.ttl, new_record.ttl)
        self.assertEqual(record.priority, new_record.priority)

    @responses.activate
    def test_get_template_record(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/templates/268/records/301',
                                           fixture_name='getTemplateRecord/success'))
        record = self.templates.get_template_record(1010, 268, 301).data

        self.assertEqual(301, record.id)
        self.assertEqual(268, record.template_id)
        self.assertIsInstance(record, TemplateRecord)

    @responses.activate
    def test_delete_template_record(self):
        responses.add(DNSimpleMockResponse(method=responses.DELETE,
                                           path='/1010/templates/268/records/301',
                                           fixture_name='deleteTemplateRecord/success'))
        self.templates.delete_template_record(1010, 268, 301)


if __name__ == '__main__':
    unittest.main()
