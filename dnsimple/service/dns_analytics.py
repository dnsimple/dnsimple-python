from dnsimple.response import Response
from dnsimple.struct import DnsAnalytics as DnsAnalyticsStruct


class DnsAnalytics(object):
    """
    The DnsAnalytics Service handles the dns_analitycs endpoint of the DNSimple API.

    See http://developer.dnsimple.com/v2/dns-analytics
    """

    def __init__(self, client):
        self.client = client

    def query(self, account_id, filter=None, sort=None, params=None, page=None, per_page=None):
        """
        Retrieves the DNS analytics of the provided account.

        See https://developer.dnsimple.com/v2/dns-analytics/#queryDnsAnalytics

        :param account_id: int
            The account ID
        :param filter: dict
            Makes it possible to ask only for the exact subset of data that you’re looking for.

            Possible filters:
                - start_date: Only include results starting from the provided date in ISO8601 format. (i.e. {'start_date': '2024-02-01'} )
                - end_date: Only include results up to the provided date in ISO8601 format (i.e. {'end_date': '2024-03-01'} )

            These filters are optional and should be used together.
        :param params: dict
            Makes it change the shape of the obtained results

            Possible params:
                - groupings: Group results by the provided list of attributes separated by a comma. Possible attributes
                             are: date, zone_name. (i.e. {'groupings': 'date,zone_name'} )
        :param sort: str
            Comma separated key-value pairs: the name of a field and the order criteria (asc for ascending and desc for
            descending).

            Possible sort criteria:
                - date: Sort results by date (i.e. 'date:asc')
                - zone_name: Sort results by zone name (alphabetical order) (i.e. 'zone_name:desc')
                - volume: Sort results by volume (i.e. 'volume:asc')
        :param page: int
            The page to return (default: 1)
        :param per_page: int
            The number of entries to return per page (default: 1000, maximum: 10000)

        :return: dnsimple.Response
            A list of domains
        """
        response = self.client.get(f'/{account_id}/dns_analytics', sort=sort, filter=filter, params=params, page=page,
                                   per_page=per_page)
        return Response(response, DnsAnalyticsStruct)
