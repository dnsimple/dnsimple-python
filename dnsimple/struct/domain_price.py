from dataclasses import dataclass

from dnsimple.struct import Struct


@dataclass
class DomainPrice(Struct):
    """
    DomainPrice represents the registration, transfer, and renewal prices.
    """

    domain = None
    """The domain name"""
    premium = None
    """If the domain name is premium return True"""
    registartion_price = None
    """The domain's registation price"""
    renewal_price = None
    """The domain's renewal price"""
    transfer_price = None
    """The domain's transfer price"""
    def __init__(self, data):
        super().__init__(data)
