import json
from dataclasses import dataclass

import omitempty

from dnsimple.struct import Struct


class DomainTransferRequest(dict):
    """DomainTransferRequest represents the attributes you can pass to a register API request."""

    def __init__(self, registrant_id, auth_code, whois_privacy=False, auto_renew=False, extended_attributes=None,
                 premium_price=None):
        dict.__init__(self, registrant_id=registrant_id, auth_code=auth_code, whois_privacy=whois_privacy,
                      auto_renew=auto_renew, extended_attributes=extended_attributes, premium_price=premium_price)

    def to_json(self):
        return json.dumps(omitempty(self))


@dataclass
class DomainTransfer(Struct):
    """Represents the result of a domain transfer call."""
    id = None
    """The domain transfer ID in DNSimple"""
    domain_id = None
    """The associated domain ID"""
    registrant_id = None
    """The associated registrant (contact) ID"""
    state = None
    """The state of the renewal"""
    auto_renew = False
    """True if the domain auto-renew was requested"""
    whois_privacy = False
    """True if the domain WHOIS privacy was requested"""
    created_at = None
    """When the domain transfer was created in DNSimple"""
    updated_at = None
    """When the domain transfer was last updated in DNSimple"""

    def __init__(self, data):
        super().__init__(data)
