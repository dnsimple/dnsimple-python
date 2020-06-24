import unittest

import responses

from dnsimple.response import Pagination
from dnsimple.struct import Service
from tests.helpers import DNSimpleMockResponse, DNSimpleTest


class ServicesTest(DNSimpleTest):
    @responses.activate
    def test_list_services(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/services',
                                           fixture_name='listServices/success'))
        services = self.services.list_services().data

        self.assertEqual(2, len(services))
        self.assertIsInstance(services[0], Service)

    @responses.activate
    def test_list_services_supports_pagination(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/services?page=1&per_page=2',
                                           fixture_name='listServices/success'))
        response = self.services.list_services(page=1, per_page=2)
        self.assertIsInstance(response.pagination, Pagination)

    @responses.activate
    def test_list_services_supports_sorting(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/services?sort=id:asc,sid:desc',
                                           fixture_name='listServices/success'))
        self.services.list_services(sort='id:asc,sid:desc')

    @responses.activate
    def test_get_service(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/services/1',
                                           fixture_name='getService/success'))
        service = self.services.get_service(1).data

        self.assertEqual(1, service.id)
        self.assertEqual('Service 1', service.name)
        self.assertEqual('service1', service.sid)
        self.assertEqual('First service example.', service.description)
        self.assertIsNone(service.setup_description)
        self.assertTrue(service.requires_setup)
        self.assertIsNone(service.default_subdomain)
        self.assertEqual('2014-02-14T19:15:19Z', service.created_at)
        self.assertEqual('2016-03-04T09:23:27Z', service.updated_at)
        self.assertEqual(1, len(service.settings))

        setting = service.settings[0]
        self.assertEqual('username', setting.name)
        self.assertEqual('Service 1 Account Username', setting.label)
        self.assertEqual('.service1.com', setting.append)
        self.assertEqual('Your Service 1 username is used to connect services to your account.', setting.description)
        self.assertEqual('username', setting.example)
        self.assertFalse(setting.password)


if __name__ == '__main__':
    unittest.main()
