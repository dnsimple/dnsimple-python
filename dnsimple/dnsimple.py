#!/usr/bin/env python
"""
Client for DNSimple REST API
https://dnsimple.com/documentation/api
"""

__version__ = '0.1.0'


import base64
from urllib2 import Request, urlopen, URLError
import re
from BaseHTTPServer import BaseHTTPRequestHandler
# Update Pythons list of error codes with some that are missing
newhttpcodes = {
    422: ('Unprocessable Entity', 'HTTP_UNPROCESSABLE_ENTITY'),
    423: ('Locked', 'HTTP_LOCKED'),
    424: ('Failed Dependency', 'HTTP_FAILED_DEPENDENCY'),
    425: ('No code', 'HTTP_NO_CODE'),
    426: ('Upgrade Required', 'HTTP_UPGRADE_REQUIRED'),
}
for code in newhttpcodes:
    BaseHTTPRequestHandler.responses[code] = newhttpcodes[code]

try:
    # Use stdlib's json if available (2.6+)
    import json
except ImportError:
    # Otherwise require extra simplejson library
    import simplejson as json


class DNSimpleException(Exception):
    pass


class DNSimple(object):

    def __init__(self,
            username=None, password=None,  # HTTP Basic Auth
            email=None, api_token=None):   # API Token Auth
        """
        Create authenticated API client.

        Provide `email` and `api_token` to use X-DNSimple-Token auth.
        Provide `username` and `password` to use HTTP Basic auth.

        If neither username/password nor api_token credentials are provided,
        the username/password will be read from the .dnsimple file.

        If both username/password and email/api_token credentials are provided,
        the API authentication credentials are preferred.
        """
        self.__endpoint = 'https://dnsimple.com'
        self.__useragent = 'DNSimple Python API v20120827'
        self.__email, self.__api_token = email, api_token
        if email is None and api_token is None:
            if username is None and password is None:
                try:
                    passwordfile = open('.dnsimple').read()
                    username = re.findall(r'username:.*',
                        passwordfile)[0].split(':')[1].strip()
                    password = re.findall(r'password:.*',
                        passwordfile)[0].split(':')[1].strip()
                except Exception, ex:
                    raise DNSimpleException(
                            'Could not open .dnsimple file: %s' % ex)
            self.__authstring = self.__getauthstring(
                self.__endpoint, username, password)

    def __getauthstring(self, __endpoint, username, password):
        encodedstring = base64.encodestring(username + ':' + password)[:-1]
        return "Basic %s" % encodedstring

    def __getauthheader(self):
        """
        Return a HTTP Basic or X-DNSimple-Token authentication header dict.
        """
        if self.__api_token:
            return {'X-DNSimple-Token': '%s:%s'
                    % (self.__email, self.__api_token)}
        else:
            return {'Authorization': self.__authstring}

    def __resthelper(self, url, postdata=None, method=None):
        """
        Does GET requests and (if postdata specified) POST requests.

        For POSTs we do NOT encode our data, as DNSimple's REST API expects
        square brackets which are normally encoded according to RFC 1738.
        urllib.urlencode encodes square brackets which the API doesn't like.
        """
        url = self.__endpoint + url
        headers = self.__getauthheader()
        headers.update({
            "User-Agent": self.__useragent,
            "Accept": "application/json",  # Accept required per doco
            })
        request = Request(url, postdata, headers)
        if method is not None:
            request.get_method = lambda: method
        result = self.__requesthelper(request)
        if result:
            return json.loads(result)
        else:
            return None

    def __requesthelper(self, request):
        """Does requests and maps HTTP responses into delicious Python juice"""
        try:
            handle = urlopen(request)
        except URLError, e:
            # Check returned URLError for issues and report 'em
            if hasattr(e, 'reason'):
                raise DNSimpleException(
                    'Failed to reach a server: %s'
                    % e.reason)
            elif hasattr(e, 'code'):
                raise DNSimpleException(
                    'Error code %s: %s'
                    % (e.code, BaseHTTPRequestHandler.responses[e.code]))
        else:
            return handle.read()

    def _prepare_data_dict(self, data, keyname):
        """
        Return formatted string from given data dict with key names suitable
        for use in API calls.

        If data provided is a string, it is returned unchanged assuming it
        is already of the correct format.

        Basically just converts key/value pairs {'a': 'v1', 'b': 'v2'} to
        have the 'KEYNAME[X]' key name formatting, for example Record API
        data would end up as {'record[a]': 'v1', 'record[b]': 'v2'}
        """
        if isinstance(data, basestring):
            return data
        prepared_data = {}
        for key, value in data.items():
            if not key.startswith('%s[' % keyname):
                key = '%s[%s]' % (keyname, key)
            prepared_data[key] = str(value)
        return '&'.join(['='.join(i) for i in prepared_data.items()])

    # DOMAINS

    def domains(self):
        """Get a list of all domains in your account."""
        return self.__resthelper('/domains')
    getdomains = domains  # Alias for backwards-compatibility

    def domain(self, id_or_domainname):
        """Get the details for a specific domain in your account. ."""
        return self.__resthelper('/domains/' + id_or_domainname)
    getdomain = domain  # Alias for backwards-compatibility

    def add_domain(self, domainname):
        """Create a single domain in DNSimple in your account."""
        postdata = 'domain[name]=' + domainname
        return self.__resthelper('/domains', postdata)
    adddomain = add_domain  # Alias for backwards-compatibility

    def check(self, domainname):
        """ Check if domain is available for registration """
        return self.__resthelper('/domains/' + domainname + '/check')

    def register(self, domainname, registrant_id=None):
        """
        Register a domain name with DNSimple and the appropriate
        domain registry.
        """
        if not registrant_id:
            # Get the registrant ID from the first domain in the acount
            try:
                registrant_id = self.getdomains()[0]['domain']['registrant_id']
            except Exception, ex:
                raise DNSimpleException(
                    'Could not find registrant_id! Please specify manually: %s'
                    % ex)
        postdata = ('domain[name]=' + domainname
                    + '&domain[registrant_id]=' + str(registrant_id))
        return self.__resthelper('/domain_registrations', postdata)

    def transfer(self, domainname, registrant_id):
        """
        Transfer a domain name from another domain registrar into DNSimple.
        """
        postdata = ('domain[name]=' + domainname
                    + '&domain[registrant_id]=' + registrant_id)
        return self.__resthelper('/domain_transfers', postdata)

    def delete(self, id_or_domainname):
        """
        Delete the given domain from your account. You may use either the
        domain ID or the domain name.
        """
        return self.__resthelper('/domains/' + id_or_domainname,
            method='DELETE')

    # RECORDS

    def records(self, id_or_domainname):
        """ Get the list of records for the specific domain """
        return self.__resthelper('/domains/' + id_or_domainname + '/records')
    getrecords = records  # Alias for backwards-compatibility

    def record(self, id_or_domainname, record_id):
        """ Get details about a specific record """
        return self.__resthelper(
            '/domains/' + id_or_domainname + '/records/' + str(record_id))
    getrecorddetail = record  # Alias for backwards-compatibility

    def add_record(self, id_or_domainname, data):
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
        data = self._prepare_data_dict(data, 'record')
        return self.__resthelper(
            '/domains/' + id_or_domainname + '/records',
            data, method='POST')

    def update_record(self, id_or_domainname, record_id, data):
        """
        Update the given record for the given domain.

        `data` parameter is a dictionary that may contain:
        - 'name'
        - 'content'
        - 'ttl'
        - 'prio'
        """
        data = self._prepare_data_dict(data, 'record')
        return self.__resthelper(
            '/domains/' + id_or_domainname + '/records/' + str(record_id),
            data, method='PUT')
    updaterecord = update_record  # Alias for backwards-compatibility

    def delete_record(self, id_or_domainname, record_id):
        """ Delete the record with the given ID for the given domain """
        return self.__resthelper(
            '/domains/' + id_or_domainname + '/records/' + str(record_id),
            method='DELETE')
