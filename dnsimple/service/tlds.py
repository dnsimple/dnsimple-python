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


class Tlds(object):
    def __init__(self, client):
        self.client = client

    def list_tlds(self, *, sort=None):
        """
        Lists TLDs supported for registration or transfer.

        See https://developer.dnsimple.com/v2/tlds/#listTlds

        """
        response = self.client.get(f"/tlds")
        return Response(response, types.TLD)

    def get_tld(self, tld: str):
        """
        Retrieves the details of a TLD.

        See https://developer.dnsimple.com/v2/tlds/#getTld

        :param tld:
            The TLD string
        """
        response = self.client.get(f"/tlds/{tld}")
        return Response(response, types.TLD)

    def get_tld_extended_attributes(self, tld: str):
        """
        Lists a TLD extended attributes.

        Some TLDs require extended attributes when registering or transferring a domain. This API interface provides information on the extended attributes for any particular TLD. Extended attributes are extra TLD-specific attributes, required by the TLD registry to collect extra information about the registrant or legal agreements.

        See https://developer.dnsimple.com/v2/tlds/#getTldExtendedAttributes

        :param tld:
            The TLD string
        """
        response = self.client.get(f"/tlds/{tld}/extended_attributes")
        return Response(response, types.ExtendedAttribute)
