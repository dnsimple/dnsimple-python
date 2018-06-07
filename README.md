Python DNSimple
===============

[![Build Status](https://travis-ci.org/onlyhavecans/dnsimple-python.svg?branch=master)](https://travis-ci.org/onlyhavecans/dnsimple-python)

## Introduction

This is a client for the [DNSimple REST API](https://developer.dnsimple.com/). It currently allows you to fetch existing domain info, as well as register new domains and manage domain records.

`dnsimple-python` works for both python 2 & 3.

**Note:** As of 1.0.0 this now uses [DNSimple's APIv2](https://blog.dnsimple.com/2016/12/api-v2-stable/). This is incompatible with older versions of the library because of authentication changes. Please review the docs and tests before deploying to production.

### Getting started

You'll need the `json` module that is included with python version 2.6 and later, or the `simplejson` module if you are using an earlier version.

`dnsimple-python` also depends on the `requests` library.

Import the module:

```python
from dnsimple import DNSimple
```

You can provide your DNSimple credentials in one of two ways:

#### Provide email/password or api\_token credentials programmatically:

```python
# Use email/password authentication: HTTP Basic
dns = DNSimple(email=YOUR_USERNAME, password=YOUR_PASSWORD)

# Use api_token credentials
dns = DNSimple(api_token=YOUR_API_TOKEN)

# If you have many accounts you can provide account_id (661 is an example)
# You can find your account id in url (https://sandbox.dnsimple.com/a/661/account)
dns = DNSimple(email=YOUR_USERNAME, password=YOUR_PASSWORD, account_id=661)
```

##### Store you email/password or api\_token credentials in a file called `.dnsimple` in the current directory with the following data:

```
[DNSimple]
email: email@domain.com
password: yourpassword
```

Or:

```
[DNSimple]
api_token: yourapitoken
```

Or (assuming `$DNSIMPLE_EMAIL` and `$DNSIMPLE_TOKEN` are environment variables):

```
[DNSimple]
email: %(DNSIMPLE_EMAIL)s
api_token: %(DNSIMPLE_TOKEN)s
```

You then need not provide any credentials when constructing `DNSimple`:

```python
dns = DNSimple()
```

## Domain Operations

### Check out your existing domains:

Just run:

```python
domains = dns.domains()
```

Results appear as a Python dict:

```python
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
```

### Get details for a specific domain

```python
dns.domain('mikemaccana.com')
```

Results are the same as `domains()` above, but only show the domain specified.

### Check whether a domain is available

```python
dns.check('google.com')

# Hmm, looks like I'm too late to get that one...
{u'currency': u'USD',
u'currency_symbol': u'$',
u'minimum_number_of_years': 1,
u'name': u'google.com',
u'price': u'14.00',
u'status': u'unavailable'}
```

### Register a new domain

```python
dns.register('newdomain.com')
```

This will register 'newdomain.com', automatically picking the registrant\_id from your first domain. To specify a particularly `registrant_id`, just run:

```python
dns.register('newdomain.com', 99)
```

Responses will be in a dictionary describing the newly created domain, same as the `domain()` call above.

### Delete a domain

Careful with this one!

```python
dns.delete('domain-to-die.com')
```

## Record operations

All operations on domain records are now supported:

* List records: `records(id_or_domainname)`
* Get record details: `record(id_or_domainname, record_id)`
* Add record: `add_record(id_or_domainname, data)`
* Update record: `update_record(id_or_domainname, record_id, data)`
* Delete record: `delete_record(id_or_domainname, record_id)`

## SSL Certificates

All read-only operations around ssl certificates are supported:

* [List certificates](https://developer.dnsimple.com/v2/certificates/#listCertificates): `certificates(id_or_domainname)`
* [Get certificate details](https://developer.dnsimple.com/v2/certificates/#getCertificate): `certificate(id_or_domainname, certificate_id)`
* [Download a certificate](https://developer.dnsimple.com/v2/certificates/#downloadCertificate): `download_certificate(id_or_domainname, certificate_id)`
* [Get a certificate's private key](https://developer.dnsimple.com/v2/certificates/#getCertificatePrivateKey): `certificate_private_key(id_or_domainname, certificate_id)`

## Running Tests

Before running tests, you'll need to ensure your environment is set up correctly.
Currently we do live tests against DNSimple's sandbox so you will need to set that up. This also means that running tests concurrently will cause failures.

### Set up DNSimple Sandbox account
1. If you don't already have a DNSimple sandbox account, [create one](https://sandbox.dnsimple.com/signup) and make sure to have your email address, password, and API token handy.
1. Copy the file `tests/.env.example` to `tests/.env` and supply your sandbox credentials

### Setup Python
If you don't wish to use pyenv you will want to skip this and run `tox` manually after setting up your environment

1. install [pyenv](https://github.com/pyenv/pyenv) using homebrew or git
1. `make test` to run all tests

## License

Licensed under the [MIT license](http://www.opensource.org/licenses/mit-license.php)

## Authors

* Original Author [Mike MacCana](https://github.com/mikemaccana/)
* APIv2 Support [Kirill Motkov](https://github.com/lcd1232)
* Maintainer [David Aronsohn](https://github.com/onlyhavecans)
