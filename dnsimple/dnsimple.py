#!/usr/bin/env python
"""
Client for DNSimple REST API
http://developer.dnsimple.com/overview/
"""

__version__ = '0.3.7'

import os.path
import sys

# Python 2 requires additional modules in order to be
# able to authenticate DNSimple API's SSL certificate
if (sys.version_info < (3, 0)):
    import pkg_resources
    from pkg_resources import DistributionNotFound
    dependencies = [
        'pyopenssl',
        'ndg-httpsclient',
        'pyasn1'
    ]
    pkg_resources.require(dependencies)

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
                 username=None, password=None,  # HTTP Basic auth
                 email=None, api_token=None,  # Access token auth
                 sandbox=False):  # Use the testing sandbox.
        """
        Create authenticated API client.

        Provide `email` and `api_token` to use API access token auth.
        Provide `username` and `password` to use HTTP Basic auth.

        If neither username/password nor domain/api_token credentials are
        provided, they will be read from the .dnsimple file.

        If both username/password and email/api_token credentials are provided,
        the API authentication credentials are preferred.
        """
        if sandbox:
            self.__endpoint = 'https://api.sandbox.dnsimple.com/v2'
        else:
            self.__endpoint = 'https://api.dnsimple.com/v2'

        self.__user_agent = 'DNSimple Python API {version}'.format(version=__version__)

        if email is None and api_token is None and username is None and password is None:
            defaults = dict(os.environ)
            defaults.update({
                'username': None,
                'password': None,
                'email': None,
                'api_token': None,
            })
            config = configparser.ConfigParser(defaults=defaults)
            for cfg in ['.dnsimple', os.path.expanduser('~/.dnsimple')]:
                if os.path.exists(cfg):
                    config.read(cfg)
                    break
            try:
                username = config.get('DNSimple', 'username')
                password = config.get('DNSimple', 'password')
                email = config.get('DNSimple', 'email')
                api_token = config.get('DNSimple', 'api_token')
            except configparser.NoSectionError:
                pass

        self.__email, self.__api_token = email, api_token

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
            return {'Authorization': 'Bearer {api_token}'.format(api_token=self.__api_token)}
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
        })
        # Add the 'Content-Type' header only if data is being sent
        if data:
            headers.update({
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
            raise
            raise DNSimpleException('Failed to reach a server.')

        except HTTPError:
            raise DNSimpleException('Invalid response.')

        response = handle.json()

        if 400 <= handle.status_code:
            raise DNSimpleException(response)

        return response['data']

    # ACCOUNTS

    def whoami(self):
        """Get details about the current authenticated entity used to access the API."""
        return self.__rest_helper('/whoami', method='GET')

    def account_id(self):
        """Get the account ID tied to our username."""
        accounts = self.__rest_helper('/accounts', method='GET')
        for account in accounts:
            if account['email'] == self.__email:
                return account['id']

    def accounts(self):
        """Get the accounts the current authenticated entity has access to."""
        return self.__rest_helper('/accounts', method='GET')

    # DOMAINS

    def domains(self):
        """Get a list of all domains in your account."""
        return self.__rest_helper('/{account}/domains'.format(account=self.account_id()), method='GET')

    getdomains = domains  # Alias for backwards-compatibility

    def domain(self, id_or_domain_name):
        """Get the details for a specific domain in your account. ."""
        return self.__rest_helper('/{account}/domains/{name}'.format(account=self.account_id(), name=id_or_domain_name), method='GET')

    getdomain = domain  # Alias for backwards-compatibility

    def add_domain(self, domain_name):
        """Create a single domain in DNSimple in your account."""
        data = {
            'domain': {
                'name': domain_name
            }
        }
        return self.__rest_helper('/{account}/domains'.format(account=self.account_id()), data, method='POST')

    adddomain = add_domain  # Alias for backwards-compatibility

    def check(self, domain_name):
        """ Check if domain is available for registration """
        return self.__rest_helper('/{account}/registrar/domains/{name}/check'.format(account=self.account_id(), name=domain_name), method='GET')

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
            'registrant_id': registrant_id
        }
        return self.__rest_helper('/{account}/registrar/domains/{name}/registrations'.format(account=self.account_id(), name=domain_name), data=data, method='POST')

    def transfer(self, domain_name, registrant_id):
        """
        Transfer a domain name from another domain registrar into DNSimple.
        """
        data = {
            'registrant_id': registrant_id
        }
        return self.__rest_helper('/{account}/registrar/domains/{name}/transfers'.format(account=self.account_id(), name=domain_name), data=data, method='POST')

    def delete(self, id_or_domain_name):
        """
        Delete the given domain from your account. You may use either the
        domain ID or the domain name.
        """
        return self.__rest_helper('/{account}/domains/{name}'.format(account=self.account_id(), name=id_or_domain_name), method='DELETE')

    # RECORDS

    def records(self, id_or_domain_name):
        """ Get the list of records for the specific domain """
        return self.__rest_helper('/{account}/zones/{name}/records'.format(account=self.account_id(), name=id_or_domain_name), method='GET')

    getrecords = records  # Alias for backwards-compatibility

    def record(self, id_or_domain_name, record_id):
        """ Get details about a specific record """
        return self.__rest_helper(
            '/{account}/zones/{name}/records/{id}'.format(account=self.account_id(), name=id_or_domain_name, id=record_id), method='GET')

    getrecorddetail = record  # Alias for backwards-compatibility

    def add_record(self, id_or_domain_name, data):
        """
        Create a record for the given domain.

        `data` parameter is a dictionary that must contain:
        - 'name' : E.g. domain prefix for CNAME
        - 'type' : E.g. 'MX', 'CNAME' etc
        - 'content'

        `data` may also contain:
        - 'ttl'
        - 'priority'
        - 'regions'
        """
        return self.__rest_helper('/{account}/zones/{domain}/records'
                                  .format(account=self.account_id(), domain=id_or_domain_name), data=data, method='POST')

    def update_record(self, id_or_domain_name, record_id, data):
        """
        Update the given record for the given domain.

        `data` parameter is a dictionary that may contain:
        - 'name'
        - 'content'
        - 'ttl'
        - 'priority'
        - 'regions'
        """
        return self.__rest_helper('/{account}/zones/{domain}/records/{record}'
                                  .format(account=self.account_id(), domain=id_or_domain_name, record=record_id), data=data, method='PATCH')

    updaterecord = update_record  # Alias for backwards-compatibility

    def delete_record(self, id_or_domain_name, record_id):
        """ Delete the record with the given ID for the given domain """
        return self.__rest_helper('/{account}/zones/{domain}/records/{record}'
                                  .format(account=self.account_id(), domain=id_or_domain_name, record=record_id), method='DELETE')

    # CONTACTS

    def contacts(self):
        """Get a list of all domain contacts in your account."""
        return self.__rest_helper('/{account}/contacts'.format(account=self.account_id()), method='GET')

    def contact(self, contact_id):
        """Get a domain contact."""
        return self.__rest_helper('/{account}/contacts/{contact}'.format(account=self.account_id(), contact=contact_id), method='GET')

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
        - `email`
        - `phone`
        - `fax`

        The `data` dictionary may also contain:
        - `label`
        - `address2`
        - `organization_name`
        - `job_title` is required when `organization_name` is present
        """
        return self.__rest_helper('/{account}/contacts'.format(account=self.account_id()), data=data, method='POST')

    # SSL CERTIFICATES

    def certificates(self, id_or_domain_name):
        """Get a list of all certificates for the specific domain"""
        return self.__rest_helper('/{account}/domains/{name}/certificates?sort=expires_on:desc,id:desc'.format(account=self.account_id(), name=id_or_domain_name), method='GET')

    def certificate_id(self, id_or_domain_name, id_or_certificate_name):
        """Get a list of certificate ids for a specific domain"""
        cert_ids = []
        certs = self.certificates(id_or_domain_name)

        for cert in certs:
            if cert['name'] == id_or_certificate_name:
                cert_ids.append(cert['id'])

        return cert_ids

    def certificate(self, id_or_domain_name, id_or_certificate_name):
        """
        Get the certificate for a specific domain
        
        If the ID of the certificate is given, we try to get the certificate by its ID.
        If the name of the certificate is given, we get the latest certificate, whether
        it's active or expired.
        """
        certificate_id = []
        if id_or_certificate_name.isdigit():
            certificate_id.append(id_or_certificate_name)
        else:
            certificate_id += self.certificate_id(id_or_domain_name, id_or_certificate_name)

            if len(certificate_id) == 0:
                raise DNSimpleException("Could not find a certificate id for '%s'. Please specify it manually." % id_or_certificate_name)

        return self.__rest_helper('/{account}/domains/{name}/certificates/{id}'.format(account=self.account_id(), name=id_or_domain_name, id=certificate_id[0]), method='GET')

    def private_key(self, id_or_domain_name, id_or_certificate_name):
        """
        Get the certificate's private key for a specific domain
        
        If the ID of the certificate is given, we try to get the certificate's private
        key by its certificate ID. If the name of the certificate is given, we get the
        latest certificate's private key, whether it's active or expired.
        """
        certificate_id = []
        if id_or_certificate_name.isdigit():
            certificate_id.append(id_or_certificate_name)
        else:
            certificate_id += self.certificate_id(id_or_domain_name, id_or_certificate_name)

            if len(certificate_id) == 0:
                raise DNSimpleException("Could not find a certificate id for '%s'. Please specify it manually." % id_or_certificate_name)

        return self.__rest_helper('/{account}/domains/{name}/certificates/{id}/private_key'.format(account=self.account_id(), name=id_or_domain_name, id=certificate_id[0]), method='GET')

    def certificate_withkey(self, id_or_domain_name, id_or_certificate_name):
        """
        Get the certificate and private key for a specific domain

        If the ID of the certificate is given, we try to get the certificate by its ID.
        If the name of the certificate is given, we get the latest certificate, whether
        it's active or expired.
        """
        certificate_id = []
        if id_or_certificate_name.isdigit():
            certificate_id.append(id_or_certificate_name)
        else:
            certificate_id += self.certificate_id(id_or_domain_name, id_or_certificate_name)

            if len(certificate_id) == 0:
                raise DNSimpleException("Could not find a certificate id for '%s'. Please specify it manually." % id_or_certificate_name)

        cert = self.__rest_helper('/{account}/domains/{name}/certificates/{id}'.format(account=self.account_id(), name=id_or_domain_name, id=certificate_id[0]), method='GET')
        cert[u'private_key'] = self.private_key(id_or_domain_name, id_or_certificate_name)['private_key']
        return cert
