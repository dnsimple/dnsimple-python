from dataclasses import dataclass
from dnsimple.struct import Struct


@dataclass
class RegistrantChange(Struct):
    """Represents a registrant change."""
    
    id = None
    type = None
    account_id = None
    contact_id = None
    domain_id = None
    state = None
    extended_attributes = None
    registry_owner_change = None
    irt_lock_lifted_by = None
    created_at = None
    updated_at = None
