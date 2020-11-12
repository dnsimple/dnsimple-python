## :warning: Development Warning

This project targets the development of the API client for the [DNSimple API v2](https://developer.dnsimple.com/v2/).

This version is currently under development, therefore the methods and the implementation should he considered a work-in-progress. Changes in the method naming, method signatures, public or internal APIs may happen at any time.

The code is tested with an automated test suite connected to a continuous integration tool, therefore you should not expect bugs to be merged into master. Regardless, use this library at your own risk.

# DNSimple Python Client

A Python client for the [DNSimple API v2](https://developer.dnsimple.com/v2/).

[![Build Status](https://travis-ci.com/dnsimple/dnsimple-python.svg?branch=master)](https://travis-ci.com/dnsimple/dnsimple-python)

## Installation

Where `<version>` denotes the version of the client you want to install.

To install the latest version:

```shell
pip install dnsimple
```

To install a specific version:

```shell
pip install dnsimple==2.0.1

```

## Usage

This library is a Python client you can use to interact with the [DNSimple API v2](https://developer.dnsimple.com/v2/). Here are some examples.

```python
from dnsimple import Client

client = Client(access_token='a1b2c3')

# Fetch your details
response = client.identity.whoami()             # execute the call
data = response.data                            # extract the relevant data from the response or
account = client.identity.whoami().data.account # execute the call and get the data in one line
```

### Define an account ID

```python
from dnsimple import Client

client = Client(access_token='a1b2c3')
account_id = 1010

# You can also fetch it from the whoami response
# as long as you authenticate with an Account access token
whoami = client.identity.whoami().data
account_id = whoami.account.id
```

### List your domains

```python
from dnsimple import Client

client = Client(access_token='a1b2c3')

account_id = client.identity.whoami().data.account.id
domains = client.domains.list_domains(account_id).data                           # Domains from the 1010 account (first page)
client.domains.list_domains(account_id, sort='expires_on:asc').data              # Domains from the 1010 account in ascending order by domain expiration date
client.domains.list_domains(account_id, filter={'name_like': 'example'}).data    # Domains from the 1010 account filtered by the domain name name
```

### Create a domain

```python
from dnsimple import Client

client = Client(access_token='a1b2c3')

account_id = client.identity.whoami().data.account.id
response = client.domains.create_domain(account_id, 'example.com')
domain = response.data # The newly created domain
```

### Get a domain

```python
from dnsimple import Client

client = Client(access_token='a1b2c3')

account_id = client.identity.whoami().data.account.id
domain_id = client.domains.list_domains(account_id).data[0].id
domain = client.domains.get_domain(account_id, domain_id).data # The domain you are looking for
```

## Sandbox Environment

We highly recommend testing against our [sandbox environment](https://developer.dnsimple.com/sandbox/) before using our
production environment. This will allow you to avoid real purchases, live charges on your credit card, and reduce the
chance of your running up against rate limits.

The client supports both the production and sandbox environment. To switch to sandbox pass the sandbox API host using
the `base_url` option when you construct the client:

```python
from dnsimple import Client

client = Client(base_url='https://api.sandbox.dnsimple.com', access_token="a1b2c3")
```

You can also set the sandbox environment like so:

```python
from dnsimple import Client

client = Client(sandbox=True, access_token='a1b2c3')
```

You will need to ensure that you are using an access token created in the sandbox environment.
Production tokens will *not* work in the sandbox environment.

## Setting a custom `User-Agent` header

You customize the `User-Agent` header for the calls made to the DNSimple API:

```python
from dnsimple import Client

client = Client(user_agent="my-app")
```

The value you provide will be appended to the default `User-Agent` the client uses.
For example, if you use `my-app`, the final header value will be `my-app dnsimple-python/0.1.0` (note that it will vary depending on the client version).

## License

Copyright (c) 2020 DNSimple Corporation. This is Free Software distributed under the MIT license.
