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


class VanityNameServers(object):
    def __init__(self, client):
        self.client = client

    def enable_vanity_name_servers(self, account: int, domain: str):
        """
        Enables Vanity Name Servers for the domain.

        This method sets up the appropriate A and AAAA records for the domain to provide vanity name servers, but it does not change the delegation for the domain. To change the delegation for domains to vanity name servers use the endpoints to Delegate to Vanity Name Servers or Dedelegate from Vanity Name Servers.

        See https://developer.dnsimple.com/v2/vanity/#enableVanityNameServers

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.put(f"/{account}/vanity/{domain}")
        return Response(response, types.VanityNameServer)

    def disable_vanity_name_servers(self, account: int, domain: str):
        """
        Disables Vanity Name Servers for the domain.

        This method removes the A and AAAA records required for the domain to provide vanity name servers, but it does not change the delegation for the domain. To change the delegation for domains to vanity name servers use the endpoints to Delegate to Vanity Name Servers or Dedelegate from Vanity Name Servers.

        See https://developer.dnsimple.com/v2/vanity/#disableVanityNameServers

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.delete(f"/{account}/vanity/{domain}")
        return Response(
            response,
        )
