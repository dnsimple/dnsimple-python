from dnsimple.service.identity import Whoami
from dnsimple.struct.account import Account
from dnsimple.struct.user import User
from tests.helpers import DNSimpleMockResponse
from tests.helpers import DNSimpleTest
import responses
import unittest


class IdentityTest(DNSimpleTest):
    @responses.activate
    def test_returns_whoami(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.GET,
                path="/whoami",
                fixture_name="whoami/success-account",
            )
        )
        self.assertIsInstance(self.identity.whoami().data, Whoami)

    @responses.activate
    def test_whoami_account_success(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.GET,
                path="/whoami",
                fixture_name="whoami/success-account",
            )
        )
        whoami = self.identity.whoami().data

        self.assertIsInstance(whoami.account, Account)
        self.assertIsNone(whoami.user)

    @responses.activate
    def test_whoami_user_success(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.GET, path="/whoami", fixture_name="whoami/success-user"
            )
        )
        whoami = self.identity.whoami().data

        self.assertIsInstance(whoami.user, User)
        self.assertEqual("example-user@example.com", whoami.user.email)
        self.assertIsNone(whoami.account)


if __name__ == "__main__":
    unittest.main()
