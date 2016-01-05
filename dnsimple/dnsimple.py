#!/usr/bin/env python
"""
Client for DNSimple REST API
http://developer.dnsimple.com/overview/
"""

__version__ = '0.3.6'

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
except ImportError:
    pass  # Issues with setup.py needed to import module but the `request` dependency hasn't been installed yet.


class DNSimpleException(Exception):
    pass


class DNSimple(object):
    def __init__(self,
                 username=None, password=None,  # HTTP Basic Auth
                 email=None, api_token=None,  # API Token Auth
                 domain_token=None,  # API Domain Token Auth
                 sandbox=False):  # Use the testing sandbox.
        """
        Create authenticated API client.

        Provide `email` and `api_token` to use X-DNSimple-Token auth.
        Provide `username` and `password` to use HTTP Basic auth.

        If neither username/password nor domain/api_token credentials are
        provided, they will be read from the .dnsimple file.

        If both a domain_token and api_token are provided, the api_token
        credentials are preferred.

        If both username/password and email/api_token credentials are provided,
        the API authentication credentials are preferred.
        """
        if sandbox:
            self.__endpoint = 'https://api.sandbox.dnsimple.com/v1'
        else:
            self.__endpoint = 'https://api.dnsimple.com/v1'

        self.__user_agent = 'DNSimple Python API {version}'.format(version=__version__)

        if email is None and api_token is None and domain_token is None and username is None and password is None:
            defaults = dict(os.environ)            
            defaults.update({
                'username': None,
                'password': None,
                'email': None,
                'api_token': None,
                'domain_token': None
            })
            config = configparser.ConfigParser(defaults=defaults)
            for cfg in ['.dnsimple', os.path.expanduser('~/.dnsimple')]:
                if os.path.exists(cfg):
                    config.read(cfg)
                    print("read {0}".format(cfg))
                    break
            try:
                username = config.get('DNSimple', 'username')
                password = config.get('DNSimple', 'password')
                email = config.get('DNSimple', 'email')
                api_token = config.get('DNSimple', 'api_token')
                domain_token = config.get('DNSimple', 'domain_token')
            except configparser.NoSectionError:
                pass

        self.__email, self.__api_token, self.__domain_token = email, api_token, domain_token

        if email is None and api_token is None:
            if username is None and password is None:
                raise DNSimpleException('No authentication details provided.')
            self.__auth_string = self.__get_auth_string(username, password)

    @staticmethod
    def __get_auth_string(username, password):
        encoded_string = encodebytes((username + ':' + password).encode())[:-1].decode()
        return "Basic {encoded_string}".format(encoded_string=encoded_string)

    def __get_auth_header(self):
        """
        Return a HTTP Basic or X-DNSimple-Token authentication header dict.
        """
        if self.__api_token:
            return {'X-DNSimple-Token': '{email}:{api_token}'.format(email=self.__email, api_token=self.__api_token)}
        elif self.__domain_token:
            return {'X-DNSimple-Domain-Token': '{domain_token}'.format(domain_token=self.__domain_token)}
        else:
            return {'Authorization': self.__auth_string}

    def __rest_helper(self, url, data=None, params=None, method='GET'):
        """
        Handles requests to the DNSimple API, defaults to GET requests if none
        provided.
        """

        url = self.__endpoint + url
        headers = self.__get_auth_header()
        headers.update({
            'User-Agent': self.__user_agent,
            'Accept': 'application/json',  # Accept required as per documentation
            'Content-Type': 'application/json'
        })
        request = Request(method=method, url=url, headers=headers, data=json.dumps(data), params=params)

        prepared_request = request.prepare()

        result = self.__request_helper(prepared_request)

        return result

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

        response = handle.json()

        if 400 <= handle.status_code:
            raise DNSimpleException(response)

        return response

    # DOMAINS

    def domains(self):
        """Get a list of all domains in your account."""
        return self.__rest_helper('/domains', method='GET')

    getdomains = domains  # Alias for backwards-compatibility

    def domain(self, id_or_domain_name):
        """Get the details for a specific domain in your account. ."""
        return self.__rest_helper('/domains/{name}'.format(name=id_or_domain_name), method='GET')

    getdomain = domain  # Alias for backwards-compatibility

    def add_domain(self, domain_name):
        """Create a single domain in DNSimple in your account."""
        data = {
            'domain': {
                'name': domain_name
            }
        }
        return self.__rest_helper('/domains', data, method='POST')

    adddomain = add_domain  # Alias for backwards-compatibility

    def check(self, domain_name):
        """ Check if domain is available for registration """
        return self.__rest_helper('/domains/{name}/check'.format(name=domain_name), method='GET')

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
        return self.__rest_helper('/domain_transfers', data=data, method='POST')

    def delete(self, id_or_domain_name):
        """
        Delete the given domain from your account. You may use either the
        domain ID or the domain name.
        """
        return self.__rest_helper('/domains/{name}'.format(name=id_or_domain_name), method='DELETE')

    # RECORDS

    def records(self, id_or_domain_name):
        """ Get the list of records for the specific domain """
        return self.__rest_helper('/domains/{name}/records'.format(name=id_or_domain_name), method='GET')

    getrecords = records  # Alias for backwards-compatibility

    def record(self, id_or_domain_name, record_id):
        """ Get details about a specific record """
        return self.__rest_helper(
            '/domains/{name}/records/{id}'.format(name=id_or_domain_name, id=record_id), method='GET')

    getrecorddetail = record  # Alias for backwards-compatibility

    def add_record(self, id_or_domain_name, data):
        """
        Create a record for the given domain.

        `data` parameter is a dictionary that must contain:
        - 'record_type' : E.g. 'MX', 'CNAME' etc
        - 'name' : E.g. domain prefix for CNAME
        - 'content'

        `data` may also contain:
        - 'ttl'
        - 'prio'
        """
        data = {
            'record': data
        }
        return self.__rest_helper('/domains/{domain}/records'
                                  .format(domain=id_or_domain_name), data=data, method='POST')

    def update_record(self, id_or_domain_name, record_id, data):
        """
        Update the given record for the given domain.

        `data` parameter is a dictionary that may contain:
        - 'name'
        - 'content'
        - 'ttl'
        - 'prio'
        """
        data = {
            'record': data
        }
        return self.__rest_helper('/domains/{domain}/records/{record}'
                                  .format(domain=id_or_domain_name, record=record_id), data=data, method='PUT')

    updaterecord = update_record  # Alias for backwards-compatibility

    def delete_record(self, id_or_domain_name, record_id):
        """ Delete the record with the given ID for the given domain """
        return self.__rest_helper('/domains/{domain}/records/{record}'
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
