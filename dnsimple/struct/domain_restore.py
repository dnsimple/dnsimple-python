import json
from dataclasses import dataclass

import omitempty

from dnsimple.struct import Struct


class DomainRestoreRequest(dict):
    """DomainRestoreRequest represents the attributes you can pass to a restore API request."""
    def __init__(self, premium_price=None):
        dict.__init__(self, premium_price=premium_price)

    def to_json(self):
        return json.dumps(omitempty(self))


@dataclass
class DomainRestore(Struct):

    """Represents the result of a domain restore call."""
    id = None
    """The domain registration ID in DNSimple"""
    domain_id = None
    """The associated domain ID"""
    state = None
    """The state of the restore"""
    created_at = None
    """When the domain restore was created in DNSimple"""
    updated_at = None
    """When the domain restore was last updated in DNSimple"""

    def __init__(self, data):
        super().__init__(data)
