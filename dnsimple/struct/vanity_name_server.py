from dataclasses import dataclass

from dnsimple.struct import Struct


@dataclass
class VanityNameServer(Struct):
    id = None
    """The vanity name server ID in DNSimple"""
    name = None
    """The vanity name server name"""
    ipv4 = None
    """The vanity name server IPv4"""
    ipv6 = None
    """The vanity name server IPv6"""
    created_at = None
    """When the vanity name server was created in DNSimple"""
    updated_at = None
    """When the vanity name server was last updated in DNSimple"""

    def __init__(self, data):
        super().__init__(data)
