from dataclasses import dataclass

from dnsimple.struct import Struct


@dataclass
class ZoneFile(Struct):
    """Represents a zone file"""

    zone = None
    """The zone file content"""

    def __init__(self, data):
        super().__init__(data)
