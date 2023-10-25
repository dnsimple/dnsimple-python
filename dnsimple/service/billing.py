from dnsimple.response import Response
from dnsimple.struct import Charge

class Billing(object):
    def __init__(self, client):
        self.client = client

    def list_charges(self, account: int, *, start_date=None, end_date=None, sort=None):
        """
        Lists the billing charges for the account.

        See https://developer.dnsimple.com/v2/billing/#listCharges

        :param account:
            The account id
        """
        response = self.client.get(f'/{account}/billing/charges', params={"start_date": start_date, "end_date": end_date, "sort": sort})
        return Response(response, Charge)
