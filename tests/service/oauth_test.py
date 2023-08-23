from dnsimple.service.oauth import AccessToken
from tests.helpers import DNSimpleMockResponse
from tests.helpers import DNSimpleTest
import responses
import unittest


class OauthTest(DNSimpleTest):
    @responses.activate
    def test_exchange_authorization_for_token(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.POST,
                path="/oauth/access_token",
                fixture_name="oauthAccessToken/success",
            )
        )
        self.code = "super-code"
        self.client_id = "super-service"
        self.client_secret = "super-secret"
        self.state = "super-state"
        self.redirect_uri = "super-uri"

        oauth_token = self.oauth.exchange_authorization_for_token(
            self.code, self.client_id, self.client_secret, self.state, self.redirect_uri
        ).data
        self.assertIsInstance(oauth_token, AccessToken)
        self.assertEqual("zKQ7OLqF5N1gylcJweA9WodA000BUNJD", oauth_token.access_token)
        self.assertEqual("Bearer", oauth_token.token_type)
        self.assertEqual(1, oauth_token.account_id)

    def test_authorize_url(self):
        url = self.oauth.authorize_url("great-app")

        self.assertEqual(
            "https://api.sandbox.dnsimple.com/oauth/authorize?client_id=great-app&response_type=code",
            url,
        )

    def test_authorize_url_with_params(self):
        url = self.oauth.authorize_url(
            "great-app", redirect_uri="https://example.com", state="secret"
        )

        self.assertEqual(
            "https://api.sandbox.dnsimple.com/oauth/authorize?client_id=great-app&response_type=code"
            "&redirect_url=https%3A%2F%2Fexample.com&state=secret",
            url,
        )


if __name__ == "__main__":
    unittest.main()
