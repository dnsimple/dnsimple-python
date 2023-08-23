from dnsimple.struct import Webhook
from tests.helpers import DNSimpleMockResponse
from tests.helpers import DNSimpleTest
import responses
import unittest


class WebhooksTest(DNSimpleTest):
    @responses.activate
    def test_list_webhooks(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.GET,
                path="/1010/webhooks",
                fixture_name="listWebhooks/success",
            )
        )
        webhooks = self.webhooks.list_webhooks(1010).data

        self.assertEqual(2, len(webhooks))
        self.assertIsInstance(webhooks[0], Webhook)
        self.assertEqual(1, webhooks[0].id)
        self.assertEqual(2, webhooks[1].id)

    @responses.activate
    def test_list_webhooks_supports_sorting(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.GET,
                path="/1010/webhooks?sort=id:desc",
                fixture_name="listWebhooks/success",
            )
        )
        self.webhooks.list_webhooks(1010, sort="id:desc")

    @responses.activate
    def test_create_webhook(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.POST,
                path="/1010/webhooks",
                fixture_name="createWebhook/created",
            )
        )
        webhook = Webhook.new("https://webhook.test")
        created = self.webhooks.create_webhook(1010, webhook).data

        self.assertEqual(webhook.url, created.url)

    @responses.activate
    def test_get_webhook(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.GET,
                path="/1010/webhooks/1",
                fixture_name="getWebhook/success",
            )
        )
        webhook = self.webhooks.get_webhook(1010, 1).data

        self.assertEqual(1, webhook.id)
        self.assertEqual("https://webhook.test", webhook.url)

    @responses.activate
    def test_delete_webhook(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.DELETE,
                path="/1010/webhooks/1",
                fixture_name="deleteWebhook/success",
            )
        )
        self.webhooks.delete_webhook(1010, 1)


if __name__ == "__main__":
    unittest.main()
