from dnsimple.response import Response
from dnsimple.struct import Account


class Accounts(object):
    """
    Lists the accounts the authenticated entity has access to.

    See http://developer.dnsimple.com/v2/accounts
    """
    def __init__(self, client):
        self.client = client

    def list_accounts(self):
        """
         Lists the accounts the current authenticated entity has access to.

        :return: dnsimple.Response
            The response containing the list of accounts.
        """
        response = self.client.get('/accounts')
        return Response(response, Account)
