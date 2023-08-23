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


@dataclass
class RegistrantChangeCheck(Struct):
    contact_id = None
    domain_id = None
    extended_attributes = None
    registry_owner_change = None

    def __init__(self, data):
        super().__init__(data)


@dataclass
class CreateRegistrantChangeInput(dict):
    def __init__(self, domain_id = None, contact_id = None, extended_attributes = None):
        super().__init__(domain_id=domain_id, contact_id=contact_id, extended_attributes=extended_attributes)

    def to_json(self):
        return json.dumps(omitempty(self))


@dataclass
class CheckRegistrantChangeInput(dict):
    domain_id = None
    contact_id = None

    def __init__(self, domain_id = None, contact_id = None):
        super().__init__(domain_id=domain_id, contact_id=contact_id)

    def to_json(self):
        return json.dumps(omitempty(self))
