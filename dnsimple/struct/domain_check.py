from dataclasses import dataclass

from dnsimple.struct import Struct


@dataclass
class DomainCheck(Struct):
    domain = None
    """The domain name"""
    available = False
    """True if the domain is available"""
    premium = False
    """True if the domain is a premium domain"""

    def __init__(self, data):
        super().__init__(data)
