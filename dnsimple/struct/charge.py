from dataclasses import dataclass

from dnsimple.struct import Struct


@dataclass
class Charge(Struct):
    invoiced_at = None
    total_amount = None
    balance_amount = None
    reference = None
    state = None
    items = None

    def __init__(self, data):
        super().__init__(data)


@dataclass
class ChargeItem(Struct):
    description = None
    amount = None
    product_id = None
    product_type = None
    product_reference = None

    def __init__(self, data):
        super().__init__(data)
