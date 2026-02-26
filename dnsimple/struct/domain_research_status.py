from dataclasses import dataclass

from dnsimple.struct import Struct


@dataclass
class DomainResearchStatus(Struct):
    request_id = None
    """UUID identifier for this research request"""
    domain = None
    """The domain name that was researched"""
    availability = None
    """The availability status. See https://developer.dnsimple.com/v2/domains/research/#getDomainsResearchStatus"""
    errors = None
    """Array of error messages if the domain cannot be registered or researched"""

    def __init__(self, data):
        super().__init__(data)
