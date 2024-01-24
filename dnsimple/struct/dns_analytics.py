from dataclasses import dataclass

from dnsimple.struct import Struct


@dataclass
class DnsAnalytics(Struct):
    """
    Represents DNS Analytics information.

    See https://developer.dnsimple.com/v2/dns_analytics/
    """

    volume = None
    """The volume"""
    zone = None
    """The zone name"""
    date = None
    """The date"""

    def __init__(self, data):
        super().__init__(data)
