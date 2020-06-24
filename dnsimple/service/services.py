from dnsimple.response import Response
from dnsimple.struct import Service


class Services(object):
    def __init__(self, client):
        self.client = client

    def list_services(self, sort=None, page=None, per_page=None):
        """
        List the available one-click services.

        See https://developer.dnsimple.com/v2/services/#listServices

        :param sort: str
            Comma separated key-value pairs: the name of a field and the order criteria (asc for ascending and desc for
            descending).

            Possible sort criteria:
                - id: Sort services by ID (i.e. 'id:asc')
                - sid: Sort services by sid (i.e. 'sid:desc')
        :param page: int
            The page to return (default: 1)
        :param per_page: int
            The number of entries to return per page (default: 30, maximum: 100)

        :return: dnsimple.Response
            The list of services in DNSimple
        """
        response = self.client.get('/services', sort=sort, page=page, per_page=per_page)
        return Response(response, Service)

    def get_service(self, service_id):
        """
        Gets the service with specified ID

        See https://developer.dnsimple.com/v2/services/#getService

        :param service_id: int
            The service id

        :return: dnsimple.Response
            The service requested
        """
        response = self.client.get(f'/services/{service_id}')
        return Response(response, Service)

    def applied_services(self, account_id, domain, page=None, per_page=None):
        """
        List services applied to a domain

        See https://developer.dnsimple.com/v2/services/domains/#listDomainAppliedServices

        :param account_id: int
            The account id
        :param domain: int/str
            The domain name or id
        :param page: int
            The page to return (default: 1)
        :param per_page: int
            The number of entries to return per page (default: 30, maximum: 100)
        :return: dnsimple.Response
            The list of services applied to the domain
        """
        response = self.client.get(f'/{account_id}/domains/{domain}/services', page=page, per_page=per_page)
        return Response(response, Service)

    def apply_service(self, account_id, domain, service):
        """
        Applies a service to a domain

        See https://developer.dnsimple.com/v2/services/domains/#applyServiceToDomain

        :param account_id: int
            The account id
        :param domain: int/str
            The domain name or id
        :param service: int/str
            The service name or id
        :return: dnsimple.Response
            An empty response
        """
        response = self.client.post(f'/{account_id}/domains/{domain}/services/{service}')
        return Response(response)

    def unapply_service(self, account_id, domain, service):
        """
        Un-applies a service from a domain

        See https://developer.dnsimple.com/v2/services/domains/#unapplyServiceFromDomain

        :param account_id: int
            The account id
        :param domain: int/str
            The domain name or id
        :param service: int/str
            The service name or id
        :return: dnsimple.Response
            An empty response
        """
        response = self.client.delete(f'/{account_id}/domains/{domain}/services/{service}')
        return Response(response)
