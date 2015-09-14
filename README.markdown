Python DNSimple
===============

## Introduction

This is a client for the DNSimple REST API. It currently allows you to fetch
existing domain info, as well as register new domains and manage domain
records.

`dnsimple-python` works for both python 2 & 3.

### Getting started

You'll need the `json` module that is included with python version 2.6 and
later, or the `simplejson` module if you are using an earlier version.

`dnsimple-python` also depends on the `requests` library.

Import the module:

	from dnsimple import DNSimple

You can provide your DNSimple credentials in one of two ways:

1. Provide username/password or email/api\_token credentials programmatically:

        # Use username/password authentication: HTTP Basic
        dns = DNSimple(username=YOUR_USERNAME, password=YOUR_PASSWORD)

        # Use email/api_token credentials
        dns = DNSimple(email=YOUR_EMAIL_ADDRESS, api_token=YOUR_API_TOKEN)

2. Store you username/password or email/api\_token credentials in a file called
`.dnsimple` in the current directory with the following data:

        [DNSimple]
        username: email@domain.com
        password: yourpassword

    Or:
    
        [DNSimple]
        email: email@domain.com
        api_token: yourapitoken

    Or (assuming `$DNSIMPLE_EMAIL` and `$DNSIMPLE_TOKEN` are environment variables):

        [DNSimple]
        email: %(DNSIMPLE_EMAIL)s
        api_token: %(DNSIMPLE_TOKEN)s

    You then need not provide any credentials when constructing `DNSimple`:

        dns = DNSimple()

## Domain Operations

### Check out your existing domains:

Just run:

	domains = dns.domains()

Results appear as a Python dict:

	{'domain': {'created_at': '2010-10-14T09:45:32Z',
	            'expires_at': '10/14/2011 5:45:00 AM',
	            'id': 999,
	            'last_enom_order_id': None,
	            'name': 'yourdomain.com',
	            'name_server_status': 'active',
	            'registrant_id': 99,
	            'registration_status': 'registered',
	            'updated_at': '2010-10-14T10:00:14Z',
	            'user_id': 99}},
	{'domain': {'created_at': '2010-10-15T16:02:34Z',
	            'expires_at': '10/15/2011 12:02:00 PM',
	            'id': 999,
	            'last_enom_order_id': None,
	            'name': 'anotherdomain.com',
	            'name_server_status': 'active',
	            'registrant_id': 99,
	            'registration_status': 'registered',
	            'updated_at': '2010-10-15T16:30:16Z',
	            'user_id': 99}}]

### Get details for a specific domain

	dns.domain('mikemaccana.com')

Results are the same as `domains()` above, but only show the domain specified.

### Check whether a domain is available

    dns.check('google.com')

    # Hmm, looks like I'm too late to get that one...
    {u'currency': u'USD',
     u'currency_symbol': u'$',
     u'minimum_number_of_years': 1,
     u'name': u'google.com',
     u'price': u'14.00',
     u'status': u'unavailable'}

### Register a new domain

	dns.register('newdomain.com')

This will register 'newdomain.com', automatically picking the registrant\_id
from your first domain. To specify a particularly `registrant_id`, just run:

	dns.register('newdomain.com', 99)

Responses will be in a dictionary describing the newly created domain, same as
the `domain()` call above.

### Delete a domain

Careful with this one!

    dns.delete('domain-to-die.com')

## Record operations

All operations on domain records are now supported:

* List records: `records(id_or_domainname)`
* Get record details: `record(id_or_domainname, record_id)`
* Add record: `add_record(id_or_domainname, data)`
* Update record: `update_record(id_or_domainname, record_id, data)`
* Delete record: `delete_record(id_or_domainname, record_id)`

### License

Licensed under the [MIT license](http://www.opensource.org/licenses/mit-license.php)
