from dataclasses import dataclass

from dnsimple.struct import Struct


@dataclass
class EmailForward(Struct):
    id = None
    """The email forward ID in DNSimple"""
    domain_id = None
    """The associated domain ID"""
    email_from = None
    """DEPRECATED: The "local part" of the originating email address. Anything to the left of the @ symbol"""
    email_to = None
    """DEPRECATED: The full email address to forward to"""
    alias_email = None
    destination_email = None
    created_at = None
    """When the email forward was created in DNSimple"""
    updated_at = None
    """When the email forward was last updated in DNSimple"""

    def __init__(self, data):
        super().__init__(data)
        setattr(self, 'email_from', data['alias_email'])
        setattr(self, 'email_to', data['destination_email'])


@dataclass
class EmailForwardInput(object):
    def __init__(self, alias_name, destination_email):
        self.alias_name = alias_name
        self.destination_email = destination_email

