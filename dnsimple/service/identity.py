from dnsimple.response import Response
from dnsimple.struct import Whoami


class Identity(object):
    """
    The Identity Service handles the identity (whoami) endpoint of the
    DNSimple API.

    See https://developer.dnsimple.com/v2/identity/
    """

    def __init__(self, client):
        """
        Initializes the service by passing the service.

        :param client: dnsimple.Client
            The service for the DNSimple API
        """
        self.client = client

    def whoami(self):
        """
        Retrieves the details about the current authenticated entity used to
        access the DNSimple API.

        :return: dnsimple.Response
            A response containing the details of the authenticated entity
        """
        response = self.client.get('/whoami')
        return Response(response, Whoami)
