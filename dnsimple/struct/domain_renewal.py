import json
from dataclasses import dataclass

import omitempty

from dnsimple.struct import Struct


class DomainRenewRequest(dict):
    """DomainRenewRequest represents the attributes you can pass to a renew API request."""
    def __init__(self, period=None, premium_price=None):
        dict.__init__(self, period=period, premium_price=premium_price)

    def to_json(self):
        return json.dumps(omitempty(self))


@dataclass
class DomainRenewal(Struct):

    """Represents the result of a domain renewal call."""
    id = None
    """The domain registration ID in DNSimple"""
    domain_id = None
    """The associated domain ID"""
    state = None
    """The state of the renewal"""
    period = None
    """The number of years the domain was registered for"""
    created_at = None
    """When the domain renewal was created in DNSimple"""
    updated_at = None
    """When the domain renewal was last updated in DNSimple"""

    def __init__(self, data):
        super().__init__(data)
