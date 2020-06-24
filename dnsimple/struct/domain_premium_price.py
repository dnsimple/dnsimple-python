from dataclasses import dataclass

from dnsimple.struct import Struct


@dataclass
class DomainPremiumPrice(Struct):
    """
    DomainPremiumPrice represents the premium price for a premium domain.
    """

    premium_price = None
    """The domain premium price"""
    action = None
    """The action (either registration, transfer or renewal)"""

    def __init__(self, data):
        super().__init__(data)


class DomainPremiumPriceOptions(dict):
    """
    DomainPremiumPriceOptions specifies the optional parameters you can provide to customize the
    dnsimple.services.Registrar.get_domain_premium_price method.
    """
    def __init__(self, action=None):
        dict.__init__(self, action=action)
