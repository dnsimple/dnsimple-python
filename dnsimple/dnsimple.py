#!/usr/bin/env python
"""
Client for DNSimple REST API
http://developer.dnsimple.com/overview/
"""
import os.path

try:
    # Use stdlib's json if available (2.6+)
    import json
except ImportError:
    # Otherwise require extra simplejson library
    import simplejson as json
try:
    from base64 import encodebytes
except ImportError:
    from base64 import encodestring as encodebytes
try:
    import ConfigParser as configparser
except ImportError:
    import configparser
try:
    from requests import Request, Session, ConnectionError, HTTPError
    from requests.auth import AuthBase, HTTPBasicAuth
except ImportError:
    pass  # Issues with setup.py needed to import module but the `request` dependency hasn't been installed yet.
except NameError:
    pass  # Issues with setup.py needed to import module but the `request.auth` dependency hasn't been installed yet.


version = (1, 0, 2)
__version__ = '.'.join(str(x) for x in version)


class DNSimpleException(Exception):
    """
    The main exception class for all exceptions we raise
    """
    pass


class DNSimpleAuthException(DNSimpleException):
    """
    Only raise this on authentication issues
    """
    pass


class DNSimpleTokenAuth(AuthBase):
    """
    Define DNSimple's token based auth
    https://developer.dnsimple.com/v2/#authentication
    """
    def __init__(self, token):
        self.token = token

    def __eq__(self, other):
        return all([
            self.token == getattr(other, 'api_key', None),
        ])

    def __ne__(self, other):
        return not self == other

    def __call__(self, r):
        r.headers['Authorization'] = 'Bearer {0!s}'.format(self.token)
        return r


class DNSimple(object):

    _account_id = None
    _auth = None
    ratelimit_limit = None
    ratelimit_remaining = None
    ratelimit_reset = None

    def __init__(self,
                 email=None, password=None,  # HTTP Basic Auth
                 api_token=None,  # API Token Auth
                 account_id=None,  # account_id if user token used
                 sandbox=False):  # Use the testing sandbox.
        """
        Create authenticated API client.

        Provide `api_token` to use OAuth2 token.
        Provide `username` and `password` to use HTTP Basic auth.

        If neither username/password nor api_token credentials are provided,
        they will be read from the .dnsimple file.

        If both username/password and api_token credentials are provided,
        the API authentication credentials are preferred.
        """
        if sandbox:
            self.__endpoint = 'https://api.sandbox.dnsimple.com/v2'
        else:
            self.__endpoint = 'https://api.dnsimple.com/v2'

        self.__user_agent = 'DNSimple Python API {version}'.format(version=__version__)

        if api_token is None and email is None and password is None and account_id is None:
            defaults = dict(os.environ)
            defaults.update({
                'email': None,
                'password': None,
                'api_token': None,
                'account_id': None,
            })
            config = configparser.ConfigParser(defaults=defaults)
            for cfg in ['.dnsimple', os.path.expanduser('~/.dnsimple')]:
                if os.path.exists(cfg):
                    config.read(cfg)
                    break
            try:
                email = config.get('DNSimple', 'email')
                password = config.get('DNSimple', 'password')
                api_token = config.get('DNSimple', 'api_token')
                account_id = config.get('DNSimple', 'account_id')
            except configparser.NoSectionError:
                pass

        self.user_account_id = account_id

        if api_token is not None:
            self._auth = DNSimpleTokenAuth(api_token)
        else:
            if email is not None and password is not None:
                self._auth = HTTPBasicAuth(email, password)
            else:
                raise DNSimpleAuthException('insufficient authentication details provided.')

    @property
    def account_id(self):
        if self._account_id is None:
            data = self.__rest_helper('/whoami', account_link=False)
            account_info = data['account']
            # This means that user use user token
            if account_info is None:
                data = self.__rest_helper('/accounts', account_link=False)
                if len(data) == 1:
                    self._account_id = data[0]['id']
                elif self.user_account_id is None:
                    raise DNSimpleException('Found many accounts for this user access token. Specify account_id.')
                else:
                    ids = [el['id'] for el in data]
                    if self.user_account_id in ids:
                        self._account_id = self.user_account_id
                    else:
                        raise DNSimpleException('Account {} not found. Possible variants: {}'.format(account_id,
                                                                                                     ', '.format(ids)))
            else:
                self._account_id = account_info['id']
        return self._account_id

    def __rest_helper(self, url, data=None, params=None, method='GET', account_link=True):
        """
        Handles requests to the DNSimple API, defaults to GET requests if none
        provided.
        """
        if account_link is True:
            url = '{endpoint}/{account_id}{url}'.format(endpoint=self.__endpoint, account_id=self.account_id, url=url)
        else:
            url = self.__endpoint + url
        headers = {
            'User-Agent': self.__user_agent,
            'Accept': 'application/json',  # Accept required as per documentation
            'Content-Type': 'application/json'
        }
        if data is not None:
            json_data = json.dumps(data)
        else:
            json_data = None
        request = Request(method=method, url=url, headers=headers, data=json_data, params=params, auth=self._auth)

        prepared_request = request.prepare()

        r_json, r_headers = self.__request_helper(prepared_request)

        if r_headers is not None:
            self.ratelimit_limit = r_headers['X-RateLimit-Limit']
            self.ratelimit_remaining = r_headers['X-RateLimit-Remaining']
            self.ratelimit_reset = r_headers['X-RateLimit-Reset']

        return r_json

    @staticmethod
    def __request_helper(request):
        """Handles firing off requests and exception raising."""
        try:
            session = Session()
            handle = session.send(request)

        except ConnectionError:
            raise DNSimpleException('Failed to reach a server.')

        except HTTPError:
            raise DNSimpleException('Invalid response.')

        # 204 code means no content
        if handle.status_code == 204:
            # Small patch for second param
            return {}, None

        response = handle.json()

        if 400 <= handle.status_code:
            raise DNSimpleException(response)

        return response['data'], handle.headers

    def __add_backward_compatibility(self, data, key):
        """
        Add backwards-compatibility
        """
        if isinstance(data, list):
            return [{key: el} for el in data]
        elif isinstance(data, dict):
            return {key: data}
        else:
            raise Exception('Unknown type: {}'.format(type(data)))

    # DOMAINS

    def domains(self):
        """
        Get a list of all domains in your account.
        """
        result = self.__rest_helper('/domains', method='GET')
        return self.__add_backward_compatibility(result, 'domain')

    getdomains = domains  # Alias for backwards-compatibility

    def domain(self, id_or_domain_name):
        """Get the details for a specific domain in your account. ."""
        # return self.__rest_helper('/domains/{name}'.format(name=id_or_domain_name), method='GET')
        result = self.__rest_helper('/domains/{name}'.format(name=id_or_domain_name), method='GET')
        return self.__add_backward_compatibility(result, 'domain')

    getdomain = domain  # Alias for backwards-compatibility

    def add_domain(self, domain_name):
        """Create a single domain in DNSimple in your account."""
        data = {
            'name': domain_name
        }
        result = self.__rest_helper('/domains', data, method='POST')
        return self.__add_backward_compatibility(result, 'domain')

    adddomain = add_domain  # Alias for backwards-compatibility

    def check(self, domain_name):
        """ Check if domain is available for registration """
        return self.__rest_helper('/registrar/domains/{name}/check'.format(name=domain_name), method='GET')

    def register(self, domain_name, registrant_id=None):
        """
        Register a domain name with DNSimple and the appropriate
        domain registry.
        """
        if not registrant_id:
            # Get the registrant ID from the first domain in the account
            try:
                registrant_id = self.getdomains()[0]['domain']['registrant_id']
            except Exception:
                raise DNSimpleException('Could not find registrant_id! Please specify manually.')

        data = {
            'name': domain_name,
            'registrant_id': registrant_id
        }
        return self.__rest_helper('/domain_registrations', data=data, method='POST')

    def transfer(self, domain_name, registrant_id):
        """
        Transfer a domain name from another domain registrar into DNSimple.
        """
        data = {
            'domain': {
                'name': domain_name,
                'registrant_id': registrant_id
            }
        }
        result = self.__rest_helper('/domain_transfers', data=data, method='POST')
        return self.__add_backward_compatibility(result, 'domain')

    def delete(self, id_or_domain_name):
        """
        Delete the given domain from your account. You may use either the
        domain ID or the domain name.
        """
        return self.__rest_helper('/domains/{name}'.format(name=id_or_domain_name), method='DELETE')

    # RECORDS

    def records(self, id_or_domain_name):
        """ Get the list of records for the specific domain """
        result = self.__rest_helper('/zones/{name}/records'.format(name=id_or_domain_name), method='GET')
        return self.__add_backward_compatibility(result, 'record')

    getrecords = records  # Alias for backwards-compatibility

    def record(self, id_or_domain_name, record_id):
        """ Get details about a specific record """
        result = self.__rest_helper(
            '/zones/{name}/records/{id}'.format(name=id_or_domain_name, id=record_id), method='GET')
        return self.__add_backward_compatibility(result, 'record')

    getrecorddetail = record  # Alias for backwards-compatibility

    def add_record(self, id_or_domain_name, data):
        """
        Create a record for the given domain.

        `data` parameter is a dictionary that must contain:
        - 'type' : E.g. 'MX', 'CNAME' etc
        - 'name' : E.g. domain prefix for CNAME
        - 'content'

        `data` may also contain:
        - 'ttl'
        - 'prio'
        - 'regions'
        """
        if 'record_type' in data:
            if 'type' not in data:
                # Backward-compatibility
                data['type'] = data.pop('record_type')
            else:
                # TODO: Print warning that need only `type`, `record_type` is deprecated
                data.pop('record_type')

        result = self.__rest_helper('/zones/{domain}/records'
                                    .format(domain=id_or_domain_name), data=data, method='POST')
        return self.__add_backward_compatibility(result, 'record')

    def update_record(self, id_or_domain_name, record_id, data):
        """
        Update the given record for the given domain.

        `data` parameter is a dictionary that may contain:
        - 'name'
        - 'content'
        - 'ttl'
        - 'prio'
        - 'regions'
        """
        return self.__rest_helper('/zones/{domain}/records/{record}'
                                  .format(domain=id_or_domain_name, record=record_id), data=data, method='PUT')

    updaterecord = update_record  # Alias for backwards-compatibility

    def delete_record(self, id_or_domain_name, record_id):
        """ Delete the record with the given ID for the given domain """
        return self.__rest_helper('/zones/{domain}/records/{record}'
                                  .format(domain=id_or_domain_name, record=record_id), method='DELETE')

    # # CONTACTS

    def contacts(self):
        """Get a list of all domain contacts in your account."""
        return self.__rest_helper('/contacts', method='GET')

    def contact(self, contact_id):
        """Get a domain contact."""
        return self.__rest_helper('/contacts/{contact}'.format(contact=contact_id), method='GET')

    def add_contact(self, data):
        """
        Create a contact that can be used as a domain registrant.

        `data` is a dictionary that must contain:
        - `first_name`
        - `last_name`
        - `address1`
        - `city`
        - `state_province`
        - `postal_code`
        - `country`
        - `email_address`
        - `phone`

        The `data` dictionary may also contain:
        - `organization_name`
        - `job_title` is required when `organization_name` is present
        - `phone_ext`
        - `fax`
        - `label`
        """
        data = {
            'contact': data
        }
        return self.__rest_helper('/contacts', data=data, method='POST')
