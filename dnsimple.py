#!/usr/bin/env python
'''Client for DNSimple REST API
https://dnsimple.com/documentation/api
'''


import base64
from urllib2 import Request, urlopen, URLError
import urllib
import re
from BaseHTTPServer import BaseHTTPRequestHandler
import simplejson as json


class DNSimple(object):
    def __init__(self,username,password):
        self.endpoint = 'https://dnsimple.com'
        self.authstring = self.getauthstring(self.endpoint,username,password)
        self.useragent = 'DNSimple Python API v20101015'

    def getauthstring(self,endpoint,username,password):
        encodedstring = base64.encodestring(username+':'+password)[:-1]
        return "Basic %s" % encodedstring

    def resthelper(self,url,postdata=None):    
        '''Does GET requests and (if postdata specified) POST requests.
        For POSTs we do NOT encode our data, as DNSimple's REST API expects square brackets
        which are normally encoded according to RFC 1738. urllib.urlencode encodes square brackets 
        which the API doesn't like.'''
        url = self.endpoint+url
        request = Request(url, postdata, {"Authorization": self.authstring, "User-Agent": self.useragent })
        result = self.requesthelper(request)
        return json.loads(result)        

    def deletehelper(self,url):    
        '''Does DELETE requests.'''
        raise Exception('Not implemented yet')
                  
    def requesthelper(self,request):
        '''Does requests and maps HTTP responses into delicious Python juice'''
        try:
            handle = urlopen(request)            
        except URLError, e:
            # Check returned URLError for issues and report 'em
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                print 'Error code: ', e.code
                print '\n'.join(BaseHTTPRequestHandler.responses[e.code])
        else:
            return handle.read()    
        
    def getdomains(self):
        '''Get a list of all domains in your account.'''
        return self.resthelper('/domains.json')

    def getdomain(self,domain):
        '''Get the details for a specific domain in your account. .'''
        return self.resthelper('/domains/'+domain+'.json')

    def getdomain(self,domain):
        '''Get the details for a specific domain in your account. .'''
        return self.resthelper('/domains/'+domain+'.json')

    def register(self,domainname,registrant_id):
        '''Register a domain name with DNSimple and the appropriate domain registry. '''
        postdata = 'domain[name]='+domainname+'&domain[registrant_id]='+registrant_id
        return self.resthelper('/domain_registrations.json', postdata)

    def transfer(self,domainname,registrant_id):
        '''Transfer a domain name from another domain registrar into DNSimple. '''
        postdata = 'domain[name]='+domainname+'&domain[registrant_id]='+registrant_id
        return self.resthelper('/domain_transfers.json', postdata)    

    def adddomains(self, domainname):
        '''Create a single domain in DNSimple in your account.'''
        postdata = 'domain[name]='+domainname
        return self.resthelper('/domains.json', postdata)          

    def delete(self,domain):
        '''Delete the given domain from your account. You may use either the domain ID or the domain name.'''
        return self.deletehelper('/domains/'+domain+'.json')
               

def main():
    passwordfile = open('.dnsimple').read()
    username = re.findall(r'username:.*', passwordfile)[0].split(':')[1].strip()
    password = re.findall(r'password:.*', passwordfile)[0].split(':')[1].strip()
    dnsimple = DNSimple(username,password) 
    print 'You should add some code here - check out the README'    
        
if __name__ == '__main__':
    main()