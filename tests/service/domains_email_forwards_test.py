from dnsimple.struct import EmailForward
from dnsimple.struct import EmailForwardInput
from tests.helpers import DNSimpleMockResponse
from tests.helpers import DNSimpleTest
import datetime
import responses
import unittest


class DomainsEmailForwardsTest(DNSimpleTest):
    @responses.activate
    def test_list_email_forwards(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.GET,
                path="/1010/domains/example.com/email_forwards",
                fixture_name="listEmailForwards/success",
            )
        )
        email_forwards = self.domains.list_email_forwards(1010, "example.com").data

        self.assertEqual(2, len(email_forwards))
        self.assertIsInstance(email_forwards[0], EmailForward)
        self.assertEqual(".*@a-domain.com", email_forwards[0].email_from)

    @responses.activate
    def test_list_email_forwards_supports_sorting(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.GET,
                path="/1010/domains/example.com" "/email_forwards?sort=from:asc",
                fixture_name="listEmailForwards/success",
            )
        )
        self.domains.list_email_forwards(1010, "example.com", sort="from:asc")

    @responses.activate
    def test_list_email_forwards_supports_pagination(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.GET,
                path="/1010/domains/example.com" "/email_forwards?page=42&per_page=1",
                fixture_name="listEmailForwards/success",
            )
        )
        self.domains.list_email_forwards(1010, "example.com", page=42, per_page=1)

    @responses.activate
    def test_create_email_forward(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.POST,
                path="/1010/domains/example.com/email_forwards",
                fixture_name="createEmailForward/created",
            )
        )
        email_forward = self.domains.create_email_forward(
            1010,
            "example.com",
            EmailForwardInput("example@dnsimple.xyz", "example@example.com"),
        ).data
        self.assertIsInstance(email_forward.id, int)
        self.assertIsInstance(email_forward.domain_id, int)
        self.assertEqual("example@dnsimple.xyz", email_forward.email_from)
        self.assertEqual("example@example.com", email_forward.email_to)
        self.assertIsInstance(
            datetime.datetime.strptime(email_forward.created_at, "%Y-%m-%dT%H:%M:%SZ"),
            datetime.datetime,
        )
        self.assertIsInstance(
            datetime.datetime.strptime(email_forward.updated_at, "%Y-%m-%dT%H:%M:%SZ"),
            datetime.datetime,
        )

    @responses.activate
    def test_get_email_forward(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.GET,
                path="/1010/domains/example.com/email_forwards/17706",
                fixture_name="getEmailForward/success",
            )
        )
        email_forward = self.domains.get_email_forward(1010, "example.com", 17706).data

        self.assertIsInstance(email_forward.domain_id, int)

    @responses.activate
    def test_delete_email_forward(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.DELETE,
                path="/1010/domains/example.com/email_forwards/17706",
                fixture_name="deleteEmailForward/success",
            )
        )
        self.domains.delete_email_forward(1010, "example.com", 17706)


if __name__ == "__main__":
    unittest.main()
