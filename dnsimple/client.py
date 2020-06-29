from urllib.parse import urljoin

from requests import Request, Session
from requests.auth import HTTPBasicAuth

from dnsimple.extra import prepare_params
from dnsimple.service import Accounts, Domains, Identity, Oauth, Zones, Registrar, Certificates, Tlds, Contacts, \
    Services, Templates, VanityNameServers, Webhooks
from dnsimple.token_authentication import TokenAuthentication
from dnsimple.version import version


class Client(object):
    """
    Client for the DNSimple API

    You can use this service to consume the services the DNSimple API
    offers. All requests have to be done authenticated. You can either
    use basic authentication (email and password combination) or an
    oauth token (see https://developer.dnsimple.com/v2/oauth/).

    service = Client(email='example-user@example.com', 'password=secret')
    user = service.identity.whoami().data.user

    service = Client(access_token='SuperSecretToken')
    account = service.identity.whoami().data.account

    For more information on how to use the DNSimple API refer
    to https://developer.dnsimple.com
    """

    __base_url = 'https://api.dnsimple.com'
    """URL to the production environment"""

    __sandbox_base_url = 'https://api.sandbox.dnsimple.com'
    """URL to the sandbox environment"""

    __api_version = 'v2'
    """Current API version"""

    __user_agent = 'dnsimple-python/{version}'
    """Default user agent for the dnsimple-python service"""

    def __init__(self,
                 email=None, password=None,
                 access_token=None,
                 base_url=None,
                 sandbox=False,
                 user_agent=None):
        """
        Initializes the service.

        You can choose which way you want to authenticate, either by email/password
        or using an OAUTH2 access token you got from the oauth 'dance'
        (see https://developer.dnsimple.com/v2/oauth/)

        :param email: str
            DNSimple email address for the account
        :param password: str
            DNSimple password for the account
        :param access_token: str
            Access token you got assigned during the oauth dance
        :param base_url: str
            A different base url you might want to use (i.e. for
            testing on the sandbox environment)
        :param sandbox: bool
            Set to true if you want to point the client to the DNSimple sandbox environment
        :param user_agent: str
            A customized 'User-Agent' header for the calls made to the DNSimple API
        """
        self._default_user_agent = self.__user_agent.format(version=version)
        self.user_agent = self._default_user_agent

        self.base_url = self.__base_url
        self.api_version = self.__api_version
        self.session = Session()
        self.__attach_services()

        self.headers = {
            'User-Agent': self.user_agent,
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

        if user_agent is not None:
            self.__change_user_agent(user_agent)

        self.base_url = self.__sandbox_base_url if sandbox is True else self.__base_url
        self.__modify_default_base_url(base_url)
        self.__add_authentication_method(access_token, email, password)

    def get(self, path, sort=None, filter=None, params=None, page=None, per_page=None):
        """
        Sends a GET request to the DNSimple API

        :param path: str
            Relative path to the service endpoint
        :param sort: str
            How to sort the response (when requesting lists)
        :param filter: dict
            Filters to be used on the request (when requesting lists)
        :param params: dict
            Query params that will be added to the request
        :param page: int
            The page to return (default: 1)
        :param per_page: int
            The number of entries to return per page (default: 30, maximum: 100)

        :return: requests.Response
            The response to the request sent
        """
        if params is None:
            params = {}
        params = {**params, **{'page': page, 'per_page': per_page}}
        request = Request(method='GET', url=self.versioned(path), headers=self.headers, auth=self.auth,
                          params=prepare_params(sort, filter, params))
        response = self.session.send(request.prepare())
        return response

    def post(self, path, data=None):
        """
        Sends a POST request to the DNSimple API

        :param path:  str
            Relative path to the service endpoint
        :param data: dict
            The data payload to send to the endpoint
        :return: requests.Response
            The response object for the request sent
        """
        request = Request(method='POST', url=self.versioned(path), headers=self.headers, auth=self.auth, data=data)
        return self.session.send(request.prepare())

    def put(self, path, data=None):
        """
        Sends a PUT request to the DNSimple API

        :param path:  str
            Relative path to the service endpoint
        :param data: obj
            The data payload to send to the endpoint
        :return: requests.Response
            The response object for the request sent
        """
        request = Request(method='PUT', url=self.versioned(path), headers=self.headers, auth=self.auth, data=data)
        return self.session.send(request.prepare())

    def patch(self, path, data=None):
        """
        Sends a PATCH request to the DNSimple API

        :param path: str
            Relative path to the service endpoint
        :param data: dict
            The data payload to send to the endpoint
        :return: requests.Response
            The response object for the request sent
        """
        request = Request(method='PATCH', url=self.versioned(path), headers=self.headers, auth=self.auth, data=data)
        return self.session.send(request.prepare())

    def delete(self, path):
        """
        Sends a DELETE request to the DNSimple API

        :param path: str
            Relative path to the service endpoint
        :return: request.Response
            The response object for the request sent
        """
        request = Request(method='DELETE', url=self.versioned(path), headers=self.headers, auth=self.auth).prepare()
        return self.session.send(request)

    def versioned(self, path):
        """
        Returns the URL to the API including the version

        :param path: str
            The relative path to the API endpoint

        :return: str
            The URL to the API including the version
        """
        versioned_base_url = urljoin(self.base_url, self.api_version)
        return '{url}/{path}'.format(url=versioned_base_url, path=path.replace('/', '', 1))

    def __change_user_agent(self, custom_user_agent_name):
        """
        Changes the User agent to a custom name.

        Note that the custom name you use will be prepended to the default
        user agent for the python service.

        :param custom_user_agent_name: str
            The custom name you want to use as your user agent
        """
        self.user_agent = '{custom_name} {user_agent}'.format(
            custom_name=custom_user_agent_name,
            user_agent=self.__user_agent.format(version=version))
        self.headers['User-Agent'] = self.user_agent

    def __modify_default_base_url(self, base_url):
        if base_url is not None:
            self.base_url = base_url

    def __add_authentication_method(self, access_token, email, password):
        if access_token is not None:
            self.auth = TokenAuthentication(access_token)
        elif email is not None and password is not None:
            self.auth = HTTPBasicAuth(email, password)

    def __attach_services(self):
        self.accounts = Accounts(self)
        self.certificates = Certificates(self)
        self.contacts = Contacts(self)
        self.domains = Domains(self)
        self.identity = Identity(self)
        self.oauth = Oauth(self)
        self.registrar = Registrar(self)
        self.services = Services(self)
        self.templates = Templates(self)
        self.tlds = Tlds(self)
        self.vanity_name_servers = VanityNameServers(self)
        self.webhooks = Webhooks(self)
        self.zones = Zones(self)
