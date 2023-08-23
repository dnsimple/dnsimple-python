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


class SecondaryDns(object):
    def __init__(self, client):
        self.client = client

    def list_primary_servers(self, account: int, *, sort=None):
        """
        List the primary servers in the account.

        See https://developer.dnsimple.com/v2/secondary-dns/#listPrimaryServers

        :param account:
            The account id
        """
        response = self.client.get(f"/{account}/secondary_dns/primaries")
        return Response(response, types.PrimaryServer)

    def create_primary_server(
        self, account: int, input: types.CreatePrimaryServerInput
    ):
        """
        Creates a primary server into the account.

        See https://developer.dnsimple.com/v2/secondary-dns/#createPrimaryServer

        :param account:
            The account id
        """
        response = self.client.post(f"/{account}/secondary_dns/primaries")
        return Response(response, types.PrimaryServer)

    def get_primary_server(self, account: int, primaryserver: int):
        """
        Retrieves the details of an existing primary server.

        See https://developer.dnsimple.com/v2/secondary-dns/#getPrimaryServer

        :param account:
            The account id
        :param primaryserver:
            The primary server id
        """
        response = self.client.get(
            f"/{account}/secondary_dns/primaries/{primaryserver}"
        )
        return Response(response, types.PrimaryServer)

    def remove_primary_server(self, account: int, primaryserver: int):
        """
        Permanently deletes a primary server.

        See https://developer.dnsimple.com/v2/secondary-dns/#removePrimaryServer

        :param account:
            The account id
        :param primaryserver:
            The primary server id
        """
        response = self.client.delete(
            f"/{account}/secondary_dns/primaries/{primaryserver}"
        )
        return Response(
            response,
        )

    def link_primary_server(self, account: int, primaryserver: int):
        """
        Link the primary server to a secondary zone.

        See https://developer.dnsimple.com/v2/secondary-dns/#linkPrimaryServer

        :param account:
            The account id
        :param primaryserver:
            The primary server id
        """
        response = self.client.put(
            f"/{account}/secondary_dns/primaries/{primaryserver}/link"
        )
        return Response(response, types.PrimaryServer)

    def unlink_primary_server(self, account: int, primaryserver: int):
        """
        Unlink the primary server from a secondary zone.

        See https://developer.dnsimple.com/v2/secondary-dns/#unlinkPrimaryServer

        :param account:
            The account id
        :param primaryserver:
            The primary server id
        """
        response = self.client.put(
            f"/{account}/secondary_dns/primaries/{primaryserver}/unlink"
        )
        return Response(response, types.PrimaryServer)

    def create_secondary_zone(
        self, account: int, input: types.CreateSecondaryZoneInput
    ):
        """
        Creates a secondary zone into the account.

        When creating a secondary zone using Solo or Teams subscription, the DNS
        services for the zone will be automatically enabled and this will be charged
        on your following subscription renewal invoices.

        See https://developer.dnsimple.com/v2/secondary-dns/#createSecondaryZone

        :param account:
            The account id
        """
        response = self.client.post(f"/{account}/secondary_dns/zones")
        return Response(response, types.Zone)
