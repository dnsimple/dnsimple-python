import json
import warnings

from dnsimple.response import Response
from dnsimple.struct import DomainResearchStatus


class DomainsResearch(object):
    """
    The DomainsResearch Service handles the domain research endpoint of the DNSimple API.
    """

    def __init__(self, client):
        self.client = client

    def domain_research_status(self, account_id, domain):
        """
        Research a domain name for availability and registration status information.

        This endpoint provides information about a domain's availability status, including whether it's available for registration, already registered, or has other restrictions that prevent registration.

        Note: This endpoint is part of a Private Beta. During the beta period, changes to the endpoint may occur at any time. If interested in using this endpoint, reach out to support@dnsimple.com.

        See https://developer.dnsimple.com/v2/domains/research/#getDomainsResearchStatus

        :param account_id: int
            The account ID
        :param domain: str
            The domain name to research

        :return: dnsimple.Response
            The domain research result
        """
        response = self.client.get(f'/{account_id}/domains/research/status', params={'domain': domain})
        return Response(response, DomainResearchStatus)
