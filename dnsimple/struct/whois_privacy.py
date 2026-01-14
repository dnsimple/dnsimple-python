from dataclasses import dataclass

from dnsimple.struct import Struct


@dataclass
class WhoisPrivacy(Struct):
    """Represents a whois privacy in DNSimple"""

    id = None
    """The whois privacy ID in DNSimple"""
    domain_id = None
    """The associated domain ID"""
    expires_on = None
    """The date the whois privacy will expire on"""
    enabled = False
    """Whether the whois privacy is enabled for the domain"""
    created_at = None
    """When the whois privacy was created in DNSimple"""
    updated_at = None
    """When the whois privacy was last updated in DNSimple"""

    def __init__(self, data):
        super().__init__(data)
