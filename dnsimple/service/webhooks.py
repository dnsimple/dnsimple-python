from dnsimple.response import Response
from dnsimple.struct import Webhook


class Webhooks(object):
    def __init__(self, client):
        self.client = client

    def list_webhooks(self, account_id, sort=None):
        """
        List the webhooks in the account

        See https://developer.dnsimple.com/v2/webhooks/#listWebhooks

        :param account_id: int
            The account id
        :param sort: str
            Comma separated key-value pairs: the name of a field and the order criteria (asc for ascending and desc for
            descending).

            Possible sort criteria:
                - id: Sort webhooks by ID (i.e. 'id:asc')

        :return: dnsimple.Response
            The list of webhooks
        """
        response = self.client.get(f'/{account_id}/webhooks', sort=sort)
        return Response(response, Webhook)

    def create_webhook(self, account_id, webhook):
        """
        Creates a webhook in the account

        See https://developer.dnsimple.com/v2/webhooks/#createWebhook

        :param account_id: int
            The account id
        :param webhook: dnsimple.struct.Webhook
            Then webhook attributes

        :return: dnsimple.Response
            The newly created webhook
        """
        response = self.client.post(f'/{account_id}/webhooks', data=webhook.to_json())
        return Response(response, Webhook)

    def get_webhook(self, account_id, webhook):
        """
        Gets a webhook from the account

        See https://developer.dnsimple.com/v2/webhooks/#getWebhook

        :param account_id: int
            The account id
        :param webhook: int/str
            The webhook id

        :return: dnsimple.Response
            The webhook
        """
        response = self.client.get(f'/{account_id}/webhooks/{webhook}')
        return Response(response, Webhook)

    def delete_webhook(self, account_id, webhook):
        """
        Deletes a webhook from the account

        See https://developer.dnsimple.com/v2/webhooks/#deleteWebhook

        :param account_id: int
            The account id
        :param webhook: int/str
            The webhook id

        :return: dnsimple.Response
            An empty response
        """
        response = self.client.delete(f'/{account_id}/webhooks/{webhook}')
        return Response(response)
