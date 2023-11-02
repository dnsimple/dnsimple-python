from dataclasses import dataclass
from decimal import Decimal

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
        if self.total_amount is not None:
            self.total_amount = Decimal(self.total_amount)
        if self.balance_amount is not None:
            self.balance_amount = Decimal(self.balance_amount)


@dataclass
class ChargeItem(Struct):
    description = None
    amount = None
    product_id = None
    product_type = None
    product_reference = None

    def __init__(self, data):
        super().__init__(data)
        if self.amount is not None:
            self.amount = Decimal(self.amount)
