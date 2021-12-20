import unittest

import responses

from dnsimple.response import Pagination
from dnsimple.struct import Template
from tests.helpers import DNSimpleMockResponse, DNSimpleTest


class TemplatesTest(DNSimpleTest):
    @responses.activate
    def test_list_templates(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/templates',
                                           fixture_name='listTemplates/success'))
        templates = self.templates.list_templates(1010).data

        self.assertEqual(2, len(templates))
        self.assertIsInstance(templates[0], Template)
        self.assertEqual(1, templates[0].id)
        self.assertEqual(2, templates[1].id)

    @responses.activate
    def test_list_templates_supports_pagination(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/templates?page=1&per_page=2',
                                           fixture_name='listTemplates/success'))
        response = self.templates.list_templates(1010, page=1, per_page=2)

        self.assertIsInstance(response.pagination, Pagination)

    @responses.activate
    def test_list_templates_supports_sorting(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/templates?sort=id:asc,name:desc,sid:asc',
                                           fixture_name='listTemplates/success'))
        self.templates.list_templates(1010, sort='id:asc,name:desc,sid:asc')

    @responses.activate
    def test_create_template(self):
        responses.add(DNSimpleMockResponse(method=responses.POST,
                                           path='/1010/templates',
                                           fixture_name='createTemplate/created'))
        template = Template.new('Beta', 'beta', 'A beta template.')
        new_template = self.templates.create_template(1010, template).data

        self.assertEqual(1, new_template.id)
        self.assertEqual(1010, new_template.account_id)
        self.assertEqual(template.name, new_template.name)
        self.assertEqual(template.sid, new_template.sid)
        self.assertEqual(template.description, new_template.description)
        self.assertEqual('2016-03-24T11:09:16Z', new_template.created_at)
        self.assertEqual('2016-03-24T11:09:16Z', new_template.updated_at)

    @responses.activate
    def test_get_template(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/templates/alpha',
                                           fixture_name='getTemplate/success'))
        template = self.templates.get_template(1010, 'alpha').data

        self.assertEqual(1, template.id)
        self.assertEqual(1010, template.account_id)
        self.assertEqual('Alpha', template.name)
        self.assertEqual('alpha', template.sid)
        self.assertEqual('An alpha template.', template.description)
        self.assertEqual('2016-03-22T11:08:58Z', template.created_at)
        self.assertEqual('2016-03-22T11:08:58Z', template.updated_at)

    @responses.activate
    def test_update_template(self):
        responses.add(DNSimpleMockResponse(method=responses.PATCH,
                                           path='/1010/templates/1',
                                           fixture_name='updateTemplate/success'))
        template = Template.new('Alpha', 'alpha', 'An alpha template.')
        updated = self.templates.update_template(1010, 1, template).data

        self.assertIsInstance(updated, Template)

    @responses.activate
    def test_delete_template(self):
        responses.add(DNSimpleMockResponse(method=responses.DELETE,
                                           path='/1010/templates/alpha',
                                           fixture_name='deleteTemplate/success'))
        self.templates.delete_template(1010, 'alpha')


if __name__ == '__main__':
    unittest.main()
