from dnsimple.client import Client
from dnsimple.struct.account import Account
from tests.helpers import DNSimpleMockResponse
from tests.helpers import DNSimpleTest
import responses
import unittest


class AccountsTest(DNSimpleTest):
    @responses.activate
    def test_list_accounts(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.GET,
                path="/accounts",
                fixture_name="listAccounts/success-account",
            )
        )
        accounts = self.accounts.list_accounts().data
        self.assertEqual(1, len(accounts))
        self.assertIsInstance(accounts[0], Account)

    @responses.activate
    def test_list_users(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.GET,
                path="/accounts",
                fixture_name="listAccounts/success-user",
            )
        )
        client = Client(
            email="tester@example.com",
            password="secret",
            base_url="https://api.sandbox.dnsimple.com",
        )
        users = client.accounts.list_accounts().data
        self.assertEqual(2, len(users))


if __name__ == "__main__":
    unittest.main()
