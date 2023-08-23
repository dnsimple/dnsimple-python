from dataclasses import dataclass
from dnsimple.struct import Struct
import json
import omitempty


@dataclass
class RegistrantChange(Struct):
    id = None
    account_id = None
    contact_id = None
    domain_id = None
    state = None
    extended_attributes = None
    registry_owner_change = None
    irt_lock_lifted_by = None
    created_at = None
    updated_at = None

    def __init__(self, data):
        super().__init__(data)

    def to_json(self):
        return json.dumps(omitempty(self))


@dataclass
class RegistrantChangeCheck(Struct):
    contact_id = None
    domain_id = None
    extended_attributes = None
    registry_owner_change = None

    def __init__(self, data):
        super().__init__(data)

    def to_json(self):
        return json.dumps(omitempty(self))


@dataclass
class ExtendedAttribute(Struct):
    name = None
    description = None
    required = None
    options = None

    def __init__(self, data):
        super().__init__(data)

    def to_json(self):
        return json.dumps(omitempty(self))


@dataclass
class ExtendedAttributeOption(Struct):
    title = None
    value = None
    description = None

    def __init__(self, data):
        super().__init__(data)

    def to_json(self):
        return json.dumps(omitempty(self))


@dataclass
class CreateRegistrantChangeInput(Struct):
    domain_id = None
    contact_id = None
    extended_attributes = None

    def __init__(self, data):
        super().__init__(data)

    def to_json(self):
        return json.dumps(omitempty(self))


@dataclass
class CheckRegistrantChangeInput(Struct):
    domain_id = None
    contact_id = None

    def __init__(self, data):
        super().__init__(data)

    def to_json(self):
        return json.dumps(omitempty(self))
