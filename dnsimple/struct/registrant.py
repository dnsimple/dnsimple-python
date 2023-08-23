from dataclasses import dataclass
from dnsimple.struct import Struct
from typing import Dict, List, Literal, Union
import json


@dataclass
class RegistrantChange(Struct):
    id: int
    account_id: int
    contact_id: int
    domain_id: int
    state: Literal["new", "pending", "cancelling", "cancelled", "completed"]
    extended_attributes: Dict[str, str]
    registry_owner_change: bool
    irt_lock_lifted_by: str
    created_at: str
    updated_at: str

    def __init__(self, data):
        super().__init__(data)

    def to_json(self):
        return json.dumps(self)


@dataclass
class RegistrantChangeCheck(Struct):
    contact_id: int
    domain_id: int
    extended_attributes: List["ExtendedAttribute"]
    registry_owner_change: bool

    def __init__(self, data):
        super().__init__(data)

    def to_json(self):
        return json.dumps(self)


@dataclass
class ExtendedAttribute(Struct):
    name: str
    description: str
    required: bool
    options: List["ExtendedAttributeOption"]

    def __init__(self, data):
        super().__init__(data)

    def to_json(self):
        return json.dumps(self)


@dataclass
class ExtendedAttributeOption(Struct):
    title: str
    value: str
    description: str

    def __init__(self, data):
        super().__init__(data)

    def to_json(self):
        return json.dumps(self)


@dataclass
class CreateRegistrantChangeInput(Struct):
    domain_id: Union[str, int]
    contact_id: Union[str, int]
    extended_attributes: Dict[str, str]

    def __init__(self, data):
        super().__init__(data)

    def to_json(self):
        return json.dumps(self)


@dataclass
class CheckRegistrantChangeInput(Struct):
    domain_id: Union[str, int]
    contact_id: Union[str, int]

    def __init__(self, data):
        super().__init__(data)

    def to_json(self):
        return json.dumps(self)
