from dataclasses import dataclass

from dnsimple.struct import Struct


@dataclass
class Zone(Struct):
    """
    Represents a Zone

    See https://developer.dnsimple.com/v2/zones
    """

    id = None
    """The zone ID in DNSimple"""
    account_id = None
    """The associated account ID in DNSimple"""
    name = None
    """The zone name"""
    reverse = None
    """True if the zone is a reverse zone"""
    created_at = None
    """When the zone was created in DNSimple"""
    updated_at = None
    """When the zone was last updated in DNSimple"""

    def __init__(self, data):
        super().__init__(data)
