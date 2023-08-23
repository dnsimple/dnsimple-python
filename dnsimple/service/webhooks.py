from dataclasses import dataclass
from dataclasses import field
from dataclasses_json import config
from dataclasses_json import dataclass_json
from dnsimple.response import Response
from typing import Any
from typing import Dict
from typing import List
from typing import Literal
from typing import Union
import dnsimple.struct as types


class Webhooks(object):
    def __init__(self, client):
        self.client = client

    def list_webhooks(self, account: int, *, sort=None):
        """
        List the webhooks in the account.

        See https://developer.dnsimple.com/v2/webhooks/webhooks/#listWebhooks

        :param account:
            The account id
        """
        response = self.client.get(f"/{account}/webhooks")
        return Response(response, types.Webhook)

    def create_webhook(self, account: int, input: types.CreateWebhookInput):
        """
        Registers a webhook endpoint.

        See https://developer.dnsimple.com/v2/webhooks/webhooks/#createWebhook

        :param account:
            The account id
        """
        response = self.client.post(f"/{account}/webhooks")
        return Response(response, types.Webhook)

    def get_webhook(self, account: int, webhook: int):
        """
        Retrieves the details of a registered webhook.

        See https://developer.dnsimple.com/v2/webhooks/webhooks/#getWebhook

        :param account:
            The account id
        :param webhook:
            The webhoook id
        """
        response = self.client.get(f"/{account}/webhooks/{webhook}")
        return Response(response, types.Webhook)

    def delete_webhook(self, account: int, webhook: int):
        """
        De-registers a webhook endpoint.

        See https://developer.dnsimple.com/v2/webhooks/webhooks/#deleteWebhook

        :param account:
            The account id
        :param webhook:
            The webhoook id
        """
        response = self.client.delete(f"/{account}/webhooks/{webhook}")
        return Response(
            response,
        )
