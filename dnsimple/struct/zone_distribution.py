from dataclasses import dataclass

from dnsimple.struct import Struct


@dataclass
class ZoneDistribution(Struct):
    """Represents the zone distribution"""

    distributed = None
    """true if the zone is properly distributed across all DNSimple name servers."""

    def __init__(self, data):
        super().__init__(data)
