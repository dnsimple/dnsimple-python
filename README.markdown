Python DNSimple
===============

## Introduction

This is a client for the DNSimple REST API. It allows you to fetch existing domain info, and register new domains. More features are on the way in future.

### Getting started

Create a file called .dnsimple in the current dir with the following data:

username: email@domain.com
password: yourpassword

Then import the module:

	from dnsimple import DNSimple
	dns = DNSimple(username,password) 

### Check out your existing domains:

Just run:

	domains = dns.getdomains()
	for domain in domains:
	    print domain['domain']['name']

### Register a new domain

Just run:

	test = dnsimple.register('google.com','16')
	
### License

Licensed under the [MIT license](http://www.opensource.org/licenses/mit-license.php)	