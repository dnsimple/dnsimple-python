import unittest

import responses

from dnsimple.struct.domain_push import DomainPushInput
from tests.helpers import DNSimpleTest, DNSimpleMockResponse


class DomainsPushesTest(DNSimpleTest):
    @responses.activate
    def test_initiate_push(self):
        responses.add(DNSimpleMockResponse(method=responses.POST,
                                           path='/2020/domains/1/pushes',
                                           fixture_name='initiatePush/success'))
        push = self.domains.initiate_push(2020, 1, DomainPushInput('admin@target-account.test')).data

        self.assertEqual(1, push.id)
        self.assertEqual(100, push.domain_id)
        self.assertIsNone(push.contact_id)
        self.assertEqual(2020, push.account_id)
        self.assertEqual('2016-08-11T10:16:03Z', push.created_at)
        self.assertEqual('2016-08-11T10:16:03Z', push.updated_at)
        self.assertIsNone(push.accepted_at)

    @responses.activate
    def test_list_pushes(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/2020/pushes',
                                           fixture_name='listPushes/success'))
        pushes = self.domains.list_pushes(2020).data

        self.assertEqual(2, len(pushes))
        self.assertEqual(101, pushes[0].domain_id)

    @responses.activate
    def test_list_pushes_supports_pagination(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/2020/pushes?page=1&per_page=2',
                                           fixture_name='listPushes/success'))
        self.domains.list_pushes(2020,  page=1, per_page=2)

    @responses.activate
    def test_accept_push(self):
        responses.add(DNSimpleMockResponse(method=responses.POST,
                                           path='/2020/pushes/42',
                                           fixture_name='acceptPush/success'))
        self.domains.accept_push(2020, 42, DomainPushInput(contact_id=3))

    @responses.activate
    def test_reject_push(self):
        responses.add(DNSimpleMockResponse(method=responses.DELETE,
                                           path='/2020/pushes/42',
                                           fixture_name='acceptPush/success'))
        self.domains.reject_push(2020, 42)


if __name__ == '__main__':
    unittest.main()
