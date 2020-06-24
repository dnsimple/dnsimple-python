import unittest

import responses

from dnsimple.struct import EmailForward, EmailForwardInput
from tests.helpers import DNSimpleTest, DNSimpleMockResponse


class DomainsEmailForwardsTest(DNSimpleTest):
    @responses.activate
    def test_list_email_forwards(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/domains/example.com/email_forwards',
                                           fixture_name='listEmailForwards/success'))
        email_forwards = self.domains.list_email_forwards(1010, 'example.com').data

        self.assertEqual(2, len(email_forwards))
        self.assertIsInstance(email_forwards[0], EmailForward)
        self.assertEqual('.*@a-domain.com', email_forwards[0].email_from)

    @responses.activate
    def test_list_email_forwards_supports_sorting(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/domains/example.com'
                                               '/email_forwards?sort=from:asc',
                                           fixture_name='listEmailForwards/success'))
        self.domains.list_email_forwards(1010, 'example.com', sort='from:asc')

    @responses.activate
    def test_list_email_forwards_supports_pagination(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/domains/example.com'
                                               '/email_forwards?page=42&per_page=1',
                                           fixture_name='listEmailForwards/success'))
        self.domains.list_email_forwards(1010, 'example.com', page=42, per_page=1)

    @responses.activate
    def test_create_email_forward(self):
        responses.add(DNSimpleMockResponse(method=responses.POST,
                                           path='/1010/domains/example.com/email_forwards',
                                           fixture_name='createEmailForward/created'))
        email_forward = self.domains.create_email_forward(1010, 'example.com',
                                                          EmailForwardInput('jim@a-domain.com', 'jim@another.com')).data
        self.assertEqual(17706, email_forward.id)
        self.assertEqual(228963, email_forward.domain_id)
        self.assertEqual('jim@a-domain.com', email_forward.email_from)
        self.assertEqual('jim@another.com', email_forward.email_to)
        self.assertEqual('2016-02-04T14:26:50Z', email_forward.created_at)
        self.assertEqual('2016-02-04T14:26:50Z', email_forward.updated_at)

    @responses.activate
    def test_get_email_forward(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/domains/example.com/email_forwards/17706',
                                           fixture_name='getEmailForward/success'))
        email_forward = self.domains.get_email_forward(1010, 'example.com', 17706).data

        self.assertEqual(228963, email_forward.domain_id)

    @responses.activate
    def test_delete_email_forward(self):
        responses.add(DNSimpleMockResponse(method=responses.DELETE,
                                           path='/1010/domains/example.com/email_forwards/17706',
                                           fixture_name='deleteEmailForward/success'))
        self.domains.delete_email_forward(1010, 'example.com', 17706)


if __name__ == '__main__':
    unittest.main()
