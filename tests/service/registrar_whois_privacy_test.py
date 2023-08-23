from dnsimple import DNSimpleException
from dnsimple.struct import WhoisPrivacy
from tests.helpers import DNSimpleMockResponse
from tests.helpers import DNSimpleTest
import responses
import unittest


class RegistrarWhoisPrivacyTest(DNSimpleTest):
    @responses.activate
    def test_get_whois_privacy(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.GET,
                path="/1010/registrar/domains/example.com/whois_privacy",
                fixture_name="getWhoisPrivacy/success",
            )
        )
        whois_privacy = self.registrar.get_whois_privacy(1010, "example.com").data

        self.assertIsInstance(whois_privacy, WhoisPrivacy)
        self.assertEqual(1, whois_privacy.id)
        self.assertEqual(2, whois_privacy.domain_id)
        self.assertEqual("2017-02-13", whois_privacy.expires_on)
        self.assertTrue(whois_privacy.enabled)
        self.assertEqual("2016-02-13T14:34:50Z", whois_privacy.created_at)
        self.assertEqual("2016-02-13T14:34:52Z", whois_privacy.updated_at)

    @responses.activate
    def test_enable_whois_privacy(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.PUT,
                path="/1010/registrar/domains/example.com/whois_privacy",
                fixture_name="enableWhoisPrivacy/success",
            )
        )
        whois_privacy = self.registrar.enable_whois_privacy(1010, "example.com").data

        self.assertTrue(whois_privacy.enabled)

    @responses.activate
    def test_enable_whois_privacy_newly_purchased(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.PUT,
                path="/1010/registrar/domains/example.com/whois_privacy",
                fixture_name="enableWhoisPrivacy/created",
            )
        )
        whois_privacy = self.registrar.enable_whois_privacy(1010, "example.com").data

        self.assertIsNone(whois_privacy.enabled)
        self.assertIsNone(whois_privacy.expires_on)

    @responses.activate
    def test_disable_whois_privacy(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.DELETE,
                path="/1010/registrar/domains/example.com/whois_privacy",
                fixture_name="disableWhoisPrivacy/success",
            )
        )
        whois_privacy = self.registrar.disable_whois_privacy(1010, "example.com").data

        self.assertFalse(whois_privacy.enabled)

    @responses.activate
    def test_renew_whois_privacy(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.POST,
                path="/1010/registrar/domains/example.com/whois_privacy",
                fixture_name="renewWhoisPrivacy/success",
            )
        )
        whois_privacy_renewal = self.registrar.renew_whois_privacy(
            1010, "example.com"
        ).data

        self.assertEqual(1, whois_privacy_renewal.id)
        self.assertEqual(100, whois_privacy_renewal.domain_id)
        self.assertEqual(999, whois_privacy_renewal.whois_privacy_id)
        self.assertEqual("new", whois_privacy_renewal.state)
        self.assertEqual("2020-01-10", whois_privacy_renewal.expires_on)
        self.assertTrue(whois_privacy_renewal.enabled)
        self.assertEqual("2019-01-10T12:12:48Z", whois_privacy_renewal.created_at)
        self.assertEqual("2019-01-10T12:12:48Z", whois_privacy_renewal.updated_at)

    @responses.activate
    def test_renew_whois_privacy_duplicated_order(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.POST,
                path="/1010/registrar/domains/example.com/whois_privacy",
                fixture_name="renewWhoisPrivacy/whois-privacy-duplicated-order",
            )
        )
        try:
            self.registrar.renew_whois_privacy(1010, "example.com")
        except DNSimpleException as dnse:
            self.assertEqual(
                "The whois privacy for example.com has just been renewed, a new renewal cannot be "
                "started at this time",
                dnse.message,
            )

    @responses.activate
    def test_renew_whois_privacy_not_found(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.POST,
                path="/1010/registrar/domains/example.com/whois_privacy",
                fixture_name="renewWhoisPrivacy/whois-privacy-not-found",
            )
        )
        try:
            self.registrar.renew_whois_privacy(1010, "example.com")
        except DNSimpleException as dnse:
            self.assertEqual("WHOIS privacy not found for example.com", dnse.message)


if __name__ == "__main__":
    unittest.main()
