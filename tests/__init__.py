import os
try:
    from ConfigParser import ConfigParser
except ImportError:
    from configparser import ConfigParser

from dnsimple import DNSimple
from .fixtures import client

env_file = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(env_file):
    parser = ConfigParser()
    parser.read(env_file)

    os.environ['DNSIMPLE_EMAIL']     = parser.get('credentials', 'email')
    os.environ['DNSIMPLE_PASSWORD']  = parser.get('credentials', 'password')
    os.environ['DNSIMPLE_API_TOKEN'] = parser.get('credentials', 'api_token')

for key in ['DNSIMPLE_EMAIL', 'DNSIMPLE_PASSWORD', 'DNSIMPLE_API_TOKEN']:
    if not os.getenv(key):
        raise Exception("Missing environment variable '{0}'".format(key))

client = client()

for domain in client.domains():
    client.delete(domain['domain']['id'])
