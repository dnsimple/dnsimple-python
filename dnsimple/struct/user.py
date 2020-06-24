from dataclasses import dataclass

from dnsimple.struct import Struct


@dataclass
class User(Struct):
    """
    Represents a User.

    See https://developer.dnsimple.com/v2/identity/
    """

    id = None
    """The ID of the user in DNSimple"""
    email = None
    """The users email"""
    created_at = None
    """When the user was created in DNSimple"""
    updated_at = None
    """When the user was last updated in DNSimple"""

    def __init__(self, data):
        super().__init__(data)
