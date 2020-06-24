import unittest

import responses

from dnsimple.response import Pagination
from dnsimple.struct import Service
from tests.helpers import DNSimpleMockResponse, DNSimpleTest


class TestName(DNSimpleTest):
    @responses.activate
    def test_applied_services(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/domains/example.com/services',
                                           fixture_name='appliedServices/success'))

        services = self.services.applied_services(1010, 'example.com').data

        self.assertEqual(1, len(services))
        self.assertIsInstance(services[0], Service)

    @responses.activate
    def test_applied_services_supports_pagination(self):

        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/domains/example.com/services?page=1&per_page=1',
                                           fixture_name='appliedServices/success'))
        response = self.services.applied_services(1010, 'example.com', page=1, per_page=1)

        self.assertIsInstance(response.pagination, Pagination)

    @responses.activate
    def test_apply_service(self):
        responses.add(DNSimpleMockResponse(method=responses.POST,
                                           path='/1010/domains/example.com/services/2',
                                           fixture_name='applyService/success'))
        response = self.services.apply_service(1010, 'example.com', 2)

        self.assertEqual('204', response.http_response.status_code)

    @responses.activate
    def test_unapply_service(self):
        responses.add(DNSimpleMockResponse(method=responses.DELETE,
                                           path='/1010/domains/example.com/services/2',
                                           fixture_name='unapplyService/success'))
        response = self.services.unapply_service(1010, 'example.com', 2)

        self.assertEqual('204', response.http_response.status_code)


if __name__ == '__main__':
    unittest.main()