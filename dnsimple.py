#!/usr/bin/env python
'''Client for DNSimple REST API
https://dnsimple.com/documentation/api
'''


import base64
from urllib2 import Request, urlopen, URLError
import urllib
import re
from BaseHTTPServer import BaseHTTPRequestHandler
# Update Pythons list of error codes with some that are missing
newhttpcodes = {
    422:('Unprocessable Entity','HTTP_UNPROCESSABLE_ENTITY'),
    423:('Locked','HTTP_LOCKED'),
    424:('Failed Dependency','HTTP_FAILED_DEPENDENCY'),
    425:('No code','HTTP_NO_CODE'),
    426:('Upgrade Required','HTTP_UPGRADE_REQUIRED'),
}
for code in newhttpcodes:
    BaseHTTPRequestHandler.responses[code] = newhttpcodes[code]

try:
    # Use stdlib's json if available (2.6+)
    import json
except ImportError:
    # Otherwise require extra simplejson library
import simplejson as json

import logging

class DNSimple(object):
    def __init__(self):
        try:
            passwordfile = open('.dnsimple').read()
            username = re.findall(r'username:.*', passwordfile)[0].split(':')[1].strip()
            password = re.findall(r'password:.*', passwordfile)[0].split(':')[1].strip()
        except: 
            logging.warn('Could not open .dnsimple file - see README.markdown')    
            exit()        
        self.__endpoint = 'https://dnsimple.com'
        self.__authstring = self.__getauthstring(self.__endpoint,username,password)
        self.__useragent = 'DNSimple Python API v20101015'

    def __getauthstring(self,__endpoint,username,password):
        encodedstring = base64.encodestring(username+':'+password)[:-1]
        return "Basic %s" % encodedstring

    def __resthelper(self,url,postdata=None,useput=False):    
        '''Does GET requests and (if postdata specified) POST requests.
        For POSTs we do NOT encode our data, as DNSimple's REST API expects square brackets
        which are normally encoded according to RFC 1738. urllib.urlencode encodes square brackets 
        which the API doesn't like.'''
        url = self.__endpoint+url
        request = Request(url, postdata, {"Authorization": self.__authstring, "User-Agent": self.__useragent })
        if useput:
            request.get_method = lambda: 'PUT'
        result = self.__requesthelper(request)
        if result:
            return json.loads(result)        
        else:
            return None

    def __deletehelper(self,url):    
        '''Does DELETE requests.'''
        raise Exception('Not implemented yet')
                  
    def __requesthelper(self,request):
        '''Does requests and maps HTTP responses into delicious Python juice'''
        try:
            handle = urlopen(request)            
        except URLError, e:
            # Check returned URLError for issues and report 'em
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
                return
            elif hasattr(e, 'code'):
                print 'Error code: ', e.code
                print '\n'.join(BaseHTTPRequestHandler.responses[e.code])
                return
        else:
            return handle.read()    
        
    def getdomains(self):
        '''Get a list of all domains in your account.'''
        return self.__resthelper('/domains.json')

    def getdomain(self,domain):
        '''Get the details for a specific domain in your account. .'''
        return self.__resthelper('/domains/'+domain+'.json')

    def getrecords(self,domain):
        '''Get the DNS records for a specfic domain in your account. .'''
        return self.__resthelper('/domains/'+domain+'/records.json')
    
    def getrecorddetail(self,domain,record):
        '''Get the details for a particular record id. .'''
        return self.__resthelper('/domain/'+domain+'/records/'+str(record))
    
    def updaterecord(self,domain,record,content):
        '''Update a record to reflect new data. .'''
        return self.__resthelper('/domains/'+domain+'/records/'+str(record),content,True)

    def getdomain(self,domain):
        '''Get the details for a specific domain in your account. .'''
        return self.__resthelper('/domains/'+domain+'.json')

    def register(self,domainname,registrant_id=None):
        '''Register a domain name with DNSimple and the appropriate domain registry. '''
        if not registrant_id:
            # Get the registrant ID from the first domain in the acount
            try:
                registrant_id = self.getdomains()[0]['domain']['registrant_id']
            except:
                print 'Could not find registrant_id! Please specify manually.'
                exit
        postdata = 'domain[name]='+domainname+'&domain[registrant_id]='+str(registrant_id)
        return self.__resthelper('/domain_registrations.json', postdata)


    def transfer(self,domainname,registrant_id):
        '''Transfer a domain name from another domain registrar into DNSimple. '''
        postdata = 'domain[name]='+domainname+'&domain[registrant_id]='+registrant_id
        return self.__resthelper('/domain_transfers.json', postdata)        

    def adddomains(self, domainname):
        '''Create a single domain in DNSimple in your account.'''
        postdata = 'domain[name]='+domainname
        return self.__resthelper('/domains.json', postdata)          

    def delete(self,domain):
        '''Delete the given domain from your account. You may use either the domain ID or the domain name.'''
        return self.__deletehelper('/domains/'+domain+'.json')
               