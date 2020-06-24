import json
from dataclasses import dataclass

import omitempty

from dnsimple.struct import Struct


@dataclass
class DomainPushInput(dict):
    """Represents the data to send to the DNSimple API to initiate a push"""

    def __init__(self, new_account_email=None, contact_id=None):
        """
        Creates a new DomainPushInput

        :param new_account_email: str
            The target account email address (Required when initiating a push)
        :param contact_id: int
            A contact that belongs to the target DNSimple account. The contact will be used as new registrant for the
            domain, if the domain is registered with DNSimple (Required when accepting a push)
        """
        dict.__init__(self, new_account_email=new_account_email, contact_id=contact_id)

    def to_json(self):
        return json.dumps(omitempty(self))


@dataclass
class DomainPush(Struct):
    """Represents a domain push"""
    id = None
    """The domain push ID in DNSimple"""
    domain_id = None
    """The associated domain ID"""
    contact_id = None
    """The associated contact ID"""
    account_id = None
    """The associated account ID"""
    created_at = None
    """When the domain push was created in DNSimple"""
    updated_at = None
    """When the domain push was last updated in DNSimple"""
    accepted_at = None
    """When the domain push was accepted in DNSimple"""

    def __init__(self, data):
        super().__init__(data)
