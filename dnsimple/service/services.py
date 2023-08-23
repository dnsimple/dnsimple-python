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


class Services(object):
    def __init__(self, client):
        self.client = client

    def list_services(self, *, sort=None):
        """
        List all available one-click services.

        See https://developer.dnsimple.com/v2/services/#listServices

        """
        response = self.client.get(f"/services")
        return Response(response, types.Service)

    def get_service(self, service: str):
        """
        Retrieves the details of a one-click service.

        See https://developer.dnsimple.com/v2/services/#getService

        :param service:
            The service sid or id
        """
        response = self.client.get(f"/services/{service}")
        return Response(response, types.Service)

    def apply_service(self, account: int, domain: str):
        """
        List services applied to a domain.

        See https://developer.dnsimple.com/v2/services/#listDomainAppliedServices

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.get(f"/{account}/domains/{domain}/services")
        return Response(response, types.Service)

    def applied_services(
        self, account: int, domain: str, service: str, input: types.AppliedServicesInput
    ):
        """
        Applies a service to a domain.

        See https://developer.dnsimple.com/v2/services/#applyServiceToDomain

        :param account:
            The account id
        :param domain:
            The domain name or id
        :param service:
            The service sid or id
        """
        response = self.client.post(f"/{account}/domains/{domain}/services/{service}")
        return Response(
            response,
        )

    def unapply_service(self, account: int, domain: str, service: str):
        """
        Unapplies a service from a domain.

        See https://developer.dnsimple.com/v2/services/#unapplyServiceFromDomain

        :param account:
            The account id
        :param domain:
            The domain name or id
        :param service:
            The service sid or id
        """
        response = self.client.delete(f"/{account}/domains/{domain}/services/{service}")
        return Response(
            response,
        )
