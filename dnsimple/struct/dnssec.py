from dataclasses import dataclass

from dnsimple.struct import Struct


@dataclass
class Dnssec(Struct):
    """
    Represents a DNSSEC for a Domain

    See https://developer.dnsimple.com/v2/domains/dnssec/
    """

    enabled = None
    """True if DNSSEC is enabled on the domain, otherwise false"""
    created_at = None
    """When the DNSSEC was created in DNSimple"""
    updated_at = None
    """When the DNSSEC was last updated in DNSimple"""

    def __init__(self, data):
        super().__init__(data)
