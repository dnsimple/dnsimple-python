from dnsimple.response import Response
from dnsimple.struct import VanityNameServer


class VanityNameServers(object):
    def __init__(self, client):
        self.client = client

    def enable_vanity_name_servers(self, account_id, domain):
        """
        Enables Vanity Name Servers for the domain

        See https://developer.dnsimple.com/v2/vanity/#enableVanityNameServers

        :param account_id: int
            The account id
        :param domain: int/str
            The domain name or id
        :return: dnsimple.Response
            The vanity name server list
        """
        response = self.client.put(f'/{account_id}/vanity/{domain}')
        return Response(response, VanityNameServer)

    def disable_vanity_name_servers(self, account_id, domain):
        """
        Disables Vanity Name Servers for the domain

        See https://developer.dnsimple.com/v2/vanity/#disableVanityNameServers

        :param account_id: int
            The account id
        :param domain: int/str
            The domain name or id

        :return: dnsimple.Response
            An empty response
        """
        response = self.client.delete(f'/{account_id}/vanity/{domain}')
        return Response(response)
