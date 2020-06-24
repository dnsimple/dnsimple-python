from dataclasses import dataclass

from dnsimple.struct import Struct


@dataclass
class Domain(Struct):
    """
    Represents a Domain

    See https://developer.dnsimple.com/v2/domains/
    """

    id = None
    """The domain ID in DNSimple"""
    account_id = None
    """The associated account ID in DNSimple"""
    registrant_id = None
    """The associated registrant (contact) ID in DNSimple"""
    name = None
    """The domain name"""
    unicode_name = None
    """The domain unicode name"""
    state = None
    """The domain state"""
    auto_renew = False
    """True if the domain is set to auto-renew, false otherwise"""
    private_whois = False
    """True if the domain WHOIS privacy is enabled, false otherwise"""
    expires_at = None
    """The date the domain will expire"""
    created_at = None
    """When the domain was created in DNSimple"""
    updated_at = None
    """When the domain was last updated in DNSimple"""

    def __init__(self, data):
        super().__init__(data)
