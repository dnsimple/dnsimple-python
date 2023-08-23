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


class Zones(object):
    def __init__(self, client):
        self.client = client

    def list_zones(self, account: int, *, name_like=None, sort=None):
        """
        Lists the zones in the account.

        See https://developer.dnsimple.com/v2/zones/#listZones

        :param account:
            The account id
        """
        response = self.client.get(f"/{account}/zones")
        return Response(response, types.Zone)

    def get_zone(self, account: int, zone: str):
        """
        Retrieves the details of an existing zone.

        See https://developer.dnsimple.com/v2/zones/#getZone

        :param account:
            The account id
        :param zone:
            The zone name
        """
        response = self.client.get(f"/{account}/zones/{zone}")
        return Response(response, types.Zone)

    def get_zone_file(self, account: int, zone: str):
        """
        Download the zonefile for an existing zone.

        See https://developer.dnsimple.com/v2/zones/#getZoneFile

        :param account:
            The account id
        :param zone:
            The zone name
        """
        response = self.client.get(f"/{account}/zones/{zone}/file")
        return Response(response, types.ZoneFile)

    def check_zone_distribution(self, account: int, zone: str):
        """
        Checks if a zone is fully distributed to all our name servers across the globe.

        See https://developer.dnsimple.com/v2/zones/#checkZoneDistribution

        :param account:
            The account id
        :param zone:
            The zone name
        """
        response = self.client.get(f"/{account}/zones/{zone}/distribution")
        return Response(response, types.ZoneDistribution)

    def update_zone_ns_records(
        self, account: int, zone: str, input: types.UpdateZoneNsRecordsInput
    ):
        """
        Updates the zone's NS records

        See https://developer.dnsimple.com/v2/zones/#updateZoneNsRecords

        :param account:
            The account id
        :param zone:
            The zone name
        """
        response = self.client.put(f"/{account}/zones/{zone}/ns_records")
        return Response(response, types.ZoneRecord)

    def list_zone_records(
        self,
        account: int,
        zone: str,
        *,
        name_like=None,
        name=None,
        type=None,
        sort=None,
    ):
        """
        Lists the records for a zone.

        See https://developer.dnsimple.com/v2/zones/#listZoneRecords

        :param account:
            The account id
        :param zone:
            The zone name
        """
        response = self.client.get(f"/{account}/zones/{zone}/records")
        return Response(response, types.ZoneRecord)

    def create_zone_record(
        self, account: int, zone: str, input: types.CreateZoneRecordInput
    ):
        """
        Creates a new zone record.

        See https://developer.dnsimple.com/v2/zones/#createZoneRecord

        :param account:
            The account id
        :param zone:
            The zone name
        """
        response = self.client.post(f"/{account}/zones/{zone}/records")
        return Response(response, types.ZoneRecord)

    def get_zone_record(self, account: int, zone: str, zonerecord: int):
        """
        Retrieves the details of an existing zone record.

        See https://developer.dnsimple.com/v2/zones/#getZoneRecord

        :param account:
            The account id
        :param zone:
            The zone name
        :param zonerecord:
            The zone record id
        """
        response = self.client.get(f"/{account}/zones/{zone}/records/{zonerecord}")
        return Response(response, types.ZoneRecord)

    def update_zone_record(
        self,
        account: int,
        zone: str,
        zonerecord: int,
        input: types.UpdateZoneRecordInput,
    ):
        """
        Updates the zone record details.

        See https://developer.dnsimple.com/v2/zones/#updateZoneRecord

        :param account:
            The account id
        :param zone:
            The zone name
        :param zonerecord:
            The zone record id
        """
        response = self.client.patch(f"/{account}/zones/{zone}/records/{zonerecord}")
        return Response(response, types.ZoneRecord)

    def delete_zone_record(
        self,
        account: int,
        zone: str,
        zonerecord: int,
        input: types.DeleteZoneRecordInput,
    ):
        """
        Permanently deletes a zone record.

        See https://developer.dnsimple.com/v2/zones/#deleteZoneRecord

        :param account:
            The account id
        :param zone:
            The zone name
        :param zonerecord:
            The zone record id
        """
        response = self.client.delete(f"/{account}/zones/{zone}/records/{zonerecord}")
        return Response(
            response,
        )

    def check_zone_record_distribution(self, account: int, zone: str, zonerecord: int):
        """
        Checks if a zone record is fully distributed to all our name servers across the globe.

        See https://developer.dnsimple.com/v2/zones/#checkZoneRecordDistribution

        :param account:
            The account id
        :param zone:
            The zone name
        :param zonerecord:
            The zone record id
        """
        response = self.client.get(
            f"/{account}/zones/{zone}/records/{zonerecord}/distribution"
        )
        return Response(response, types.ZoneDistribution)

    def activate_dns(self, account: int, zone: str):
        """
        Activate DNS services for the zone.

        Under Solo and Teams plans, active zones are charged when renewing your subscription to
        DNSimple

        See https://developer.dnsimple.com/v2/zones/#activateZoneService

        :param account:
            The account id
        :param zone:
            The zone name
        """
        response = self.client.put(f"/{account}/zones/{zone}/activation")
        return Response(response, types.Zone)

    def deactivate_dns(self, account: int, zone: str):
        """
        Deactivates DNS services for the zone.

        Under Solo and Teams plans, active zones are charged when renewing your subscription to
        DNSimple

        See https://developer.dnsimple.com/v2/zones/#deactivateZoneService

        :param account:
            The account id
        :param zone:
            The zone name
        """
        response = self.client.delete(f"/{account}/zones/{zone}/activation")
        return Response(response, types.Zone)
