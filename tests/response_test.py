import unittest

import requests
import responses

from dnsimple.extra import return_list_of
from dnsimple.response import Response, Pagination
from dnsimple.struct import Whoami, Domain
from tests.helpers import DNSimpleMockResponse


class ResponseTest(unittest.TestCase):
    @responses.activate
    def setUp(self) -> None:
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           url='https://api.sandbox.dnsimple.com/v2/whoami',
                                           fixture_name='whoami/success-user'))

        self.http_response = requests.get('https://api.sandbox.dnsimple.com/v2/whoami')
        self.dnsimple_response = Response(self.http_response, Whoami)

    def test_contains_the_response_object(self):
        self.assertIsInstance(self.dnsimple_response.data, Whoami)

    def test_contains_the_http_response(self):
        self.assertEqual(self.http_response, self.dnsimple_response.http_response)

    def test_contains_the_http_headers(self):
        self.assertEqual(self.http_response.headers, self.dnsimple_response.headers)

    def test_contains_the_rate_limit(self):
        self.assertEqual(4000, self.dnsimple_response.rate_limit)

    def test_contains_the_rate_limit_remaining(self):
        self.assertEqual(3991, self.dnsimple_response.rate_limit_remaining)

    def test_contains_the_rate_limit_reset(self):
        self.assertEqual(1450451976, self.dnsimple_response.rate_limit_reset)

    @responses.activate
    def test_contains_a_pagination_object(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           url='https://api.sandbox.dnsimple.com/v2/1010/domains',
                                           fixture_name='listDomains/success'))
        http_response = requests.get('https://api.sandbox.dnsimple.com/v2/1010/domains')
        dnsimple_response = Response(http_response, Domain)
        pagination = Pagination({'current_page': 1, 'per_page': 30, 'total_entries': 2, 'total_pages': 1})

        self.assertEqual(pagination.current_page, dnsimple_response.pagination.current_page)
        self.assertEqual(pagination.per_page, dnsimple_response.pagination.per_page)
        self.assertEqual(pagination.total_entries, dnsimple_response.pagination.total_entries)
        self.assertEqual(pagination.total_pages, dnsimple_response.pagination.total_pages)


if __name__ == '__main__':
    unittest.main()
