from dataclasses import dataclass
from dnsimple.struct.struct import Struct

@dataclass
class DomainTransferLock(Struct):
    enabled: bool

    def __init__(self, data):
        super().__init__(data)
