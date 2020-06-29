from dnsimple.response import Response
from dnsimple.struct import Zone, ZoneDistribution, ZoneFile, ZoneRecord


class Zones(object):
    """
    The Zones Service handles the zones endpoint of the DNSimple API.

    See https://developer.dnsimple.com/v2/zones
    """

    def __init__(self, client):
        self.client = client

    def list_zones(self, account_id, filter=None, sort=None, page=None, per_page=None):
        """
        Lists the zones in the account.

        See https://developer.dnsimple.com/v2/zones/#listZones

        :param account_id: int
            The account ID
        :param sort: str
            Comma separated key-value pairs: the name of a field and the order criteria (asc for ascending and desc for
            descending).

            Possible sort criteria:
                - id: Sort zones by ID (i.e. 'id:asc')
                - name: Sort zones by name (alphabetical order) (i.e. 'name:desc')
        :param filter: dict
            Makes it possible to ask only for the exact subset of data that you you’re looking for.

            Possible filters:
                - name_like: Only include zones containing given string (i.e. {'name_like': 'example.com'} )
        :param page: int
            The page to return (default: 1)
        :param per_page: int
            The number of entries to return per page (default: 30, maximum: 100)

        :return: dnsimple.Response
            The list of zones requested
        """
        response = self.client.get(f'/{account_id}/zones', filter=filter, sort=sort, page=page, per_page=per_page)
        return Response(response, Zone)

    def get_zone(self, account_id, zone):
        """
        Gets a zone from the account

        See https://developer.dnsimple.com/v2/zones/#getZone

        :param account_id: int
            The account ID
        :param zone: str
            The zone name

        :return: dnsimple.Response
            The zone requested
        """
        response = self.client.get(f'/{account_id}/zones/{zone}')
        return Response(response, Zone)

    def get_zone_file(self, account_id, zone):
        """
        Gets a zone file from the account

        See https://developer.dnsimple.com/v2/zones/#getZoneFile

        :param account_id: int
            The account ID
        :param zone: str
            The zone name

        :return: dnsimple.Response
            The zone file requested
        """
        response = self.client.get(f'/{account_id}/zones/{zone}/file')
        return Response(response, ZoneFile)

    def check_zone_distribution(self, account_id, zone):
        """
        Checks if a zone change is fully distributed to all DNSimple name servers across the globe.

        WARNING: This feature can’t be tested in our Sandbox environment.

        See https://developer.dnsimple.com/v2/zones/#checkZoneDistribution

        :param account_id: int
            The account ID
        :param zone: str
            The zone name

        :return: dnsimple.Response
            The zone distribution
        """
        response = self.client.get(f'/{account_id}/zones/{zone}/distribution')
        return Response(response, ZoneDistribution)

    def list_records(self, account_id, zone, filter=None, sort=None, page=None, per_page=None):
        """
        Lists the zone records in the account

        See https://developer.dnsimple.com/v2/zones/records/#listZoneRecords

        :param account_id: int
            The account ID
        :param zone: str
            The zone name
        :param sort: str
            Comma separated key-value pairs: the name of a field and the order criteria (asc for ascending and desc for
            descending).

            Possible sort criteria:
                - id: Sort records by ID (i.e. 'id:asc')
                - name: Sort records by name (i.e. 'name:desc')
                - content: Sort records by content (i.e. 'content:asc')
                - type: Sort records by type (i.e. 'type:asc')
        :param filter: dict
            Makes it possible to ask only for the exact subset of data that you you’re looking for.

            Possible filters:
                - name_like: Only include records where the name contains the given string (i.e.{'name_like':'example'})
                - name: Only include records with name equal to the given string (i.e. {'name': 'example.com'})
                - type: Only include records with the record type equal to the given string (i.e. {'type': 'SOA'})
        :param page: int
            The page to return (default: 1)
        :param per_page: int
            The number of entries to return per page (default: 30, maximum: 100)

        :return: dnsimple.Response
            The list of zone records in the account
        """
        response = self.client.get(f'/{account_id}/zones/{zone}/records', filter=filter, sort=sort, page=page,
                                   per_page=per_page)
        return Response(response, ZoneRecord)

    def create_record(self, account_id, zone, record):
        """
        Create a record for the zone in the account

        See https://developer.dnsimple.com/v2/zones/records/#createZoneRecord

        :param account_id: int
            The account ID
        :param zone: str
            The zone name
        :param record: dnsimple.struct.ZoneRecordInput
            The data to send to create the zone record

        :return: dnsimple.Response
            The newly created zone record
        """
        response = self.client.post(f'/{account_id}/zones/{zone}/records', data=record.to_json())
        return Response(response, ZoneRecord)

    def get_record(self, account_id, zone, record_id):
        """
        Gets a zone record from the account

        See https://developer.dnsimple.com/v2/zones/records/#getZoneRecord

        :param account_id: int
            The account ID
        :param zone: str
            The zone name
        :param record_id: int
            The record ID

        :return: dnsimple.Response
            The zone record requested
        """
        response = self.client.get(f'/{account_id}/zones/{zone}/records/{record_id}')
        return Response(response, ZoneRecord)

    def update_record(self, account_id, zone, record_id, record):
        """
        Updates a zone record in the account.

        See https://developer.dnsimple.com/v2/zones/records/#updateZoneRecord

        :param account_id: int
            The account ID
        :param zone: str
            The zone name
        :param record_id: int
            The record ID
        :param record: dnsimple.struct.ZoneRecordUpdateInput
            The data to send to update the zone record
        :return: dnsimple.Response
            The updated zone record
        """
        response = self.client.patch(f'/{account_id}/zones/{zone}/records/{record_id}', data=record.to_json())
        return Response(response, ZoneRecord)

    def delete_record(self, account_id, zone, record_id):
        """
        Deletes a zone record from the account.

        WARNING: this cannot be undone.

        See https://developer.dnsimple.com/v2/zones/records/#deleteZoneRecord

        :param account_id: int
            The account ID
        :param zone: str
            The zone name
        :param record_id: int
            The record ID
        :return: dnsimple.Response
            An empty response
        """
        response = self.client.delete(f'/{account_id}/zones/{zone}/records/{record_id}')
        return Response(response)

    def check_zone_record_distribution(self, account_id, zone, record_id):
        """
        Checks if a zone record is fully distributed to all DNSimple name servers across the globe.

        WARNING: This feature can’t be tested in our Sandbox environment.

        See https://developer.dnsimple.com/v2/zones/records/#checkZoneRecordDistribution

        :param account_id: int
            The account ID
        :param zone: str
            The zone name
        :param record_id: int
            The record ID

        :return: dnsimple.Response
            The zone record distribution
        """
        response = self.client.get(f'/{account_id}/zones/{zone}/records/{record_id}/distribution')
        return Response(response, ZoneDistribution)
