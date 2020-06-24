from dataclasses import dataclass

from dnsimple.struct import Struct


@dataclass
class EmailForward(Struct):
    id = None
    """The email forward ID in DNSimple"""
    domain_id = None
    """The associated domain ID"""
    email_from = None
    """The "local part" of the originating email address. Anything to the left of the @ symbol"""
    email_to = None
    """The full email address to forward to"""
    created_at = None
    """When the email forward was created in DNSimple"""
    updated_at = None
    """When the email forward was last updated in DNSimple"""

    def __init__(self, data):
        super().__init__(data)
        setattr(self, 'email_from', data['from'])
        setattr(self, 'email_to', self.to)


@dataclass
class EmailForwardInput(object):
    def __init__(self, email_from, email_to):
        self.email_from = email_from
        self.email_to = email_to
