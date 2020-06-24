from dataclasses import dataclass

from dnsimple.struct import Struct


@dataclass
class Account(Struct):
    """
    Represents an Account.

    See https://developer.dnsimple.com/v2/identity/
    """

    id = None
    """The account ID in DNSimple"""
    email = None
    """The account email"""
    plan_identifier = None
    """The identifier of the plan the account is subscribed to"""
    created_at = None
    """When the account was created in DNSimple"""
    updated_at = None
    """When the account was last updated in DNSimple"""

    def __init__(self, data):
        super().__init__(data)
