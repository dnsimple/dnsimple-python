from dnsimple.client import Client
from dnsimple.version import version
import unittest


class ClientTest(unittest.TestCase):
    def test_defaults_base_url_to_production_api(self):
        client = Client()
        self.assertEqual("https://api.dnsimple.com", client.base_url)

    def test_api_version(self):
        client = Client()
        self.assertEqual("v2", client.api_version)

    def test_accepts_base_url_option(self):
        client = Client(base_url="http://api.example.com")
        self.assertEqual("http://api.example.com", client.base_url)

    def test_sets_sandbox_environment(self):
        client = Client(sandbox=True)
        self.assertEqual("https://api.sandbox.dnsimple.com", client.base_url)

    def test_access_token(self):
        client = Client(access_token="token")
        self.assertEqual("token", client.auth.token)

    def test_uses_basic_authentication(self):
        client = Client(email="example-user@example.com", password="secret")
        self.assertEqual("example-user@example.com", client.auth.username)
        self.assertEqual("secret", client.auth.password)

    def test_uses_oauth2_authorization(self):
        client = Client(access_token="token")
        self.assertEqual("token", client.auth.token)

    def test_uses_versioned_url(self):
        client = Client()
        self.assertEqual(
            "https://api.dnsimple.com/v2/whoami", client.versioned("/whoami")
        )

    def test_can_set_the_user_agent(self):
        client = Client(user_agent="MySuperAPP")

        self.assertEqual(
            "MySuperAPP dnsimple-python/{version}".format(version=version),
            client.user_agent,
        )


if __name__ == "__main__":
    unittest.main()
