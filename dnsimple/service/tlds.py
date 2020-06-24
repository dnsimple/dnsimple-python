from dnsimple.response import Response
from dnsimple.struct import Tld, TldExtendedAttribute


class Tlds(object):
    """Handles communication with the Tld related methods of the DNSimple API."""

    def __init__(self, client):
        self.client = client

    def list_tlds(self, sort=None):
        """
        Lists the TLDs available for registration

        See https://developer.dnsimple.com/v2/tlds/#listTlds

        :param sort: str
            Comma separated key-value pairs: the name of a field and the order criteria (asc for ascending and desc for
            descending).

            Possible sort criteria:
                - tld: Sort TLDs by tld (i.e. 'tld:asc')

        :return: dnsimple.Response
            The tld list
        """
        response = self.client.get('/tlds', sort=sort)
        return Response(response, Tld)

    def get_tld(self, tld):
        """
        Gets the details of a TLD

        See https://developer.dnsimple.com/v2/tlds/#getTld
        
        :param tld: str
            The TLD name

        :return: dnsimple.Response
            The TLD details
        """
        response = self.client.get(f'/tlds/{tld}')
        return Response(response, Tld)

    def get_tld_extended_attributes(self, tld):
        """
        Gets the extended attributes for a TLD

        See https://developer.dnsimple.com/v2/tlds/#getTldExtendedAttributes

        :param tld: str
            The TLD name

        :return: dnsimple.Response
            The TLDs extended attributes
        """
        response = self.client.get(f'/tlds/{tld}/extended_attributes')
        return Response(response, TldExtendedAttribute)
