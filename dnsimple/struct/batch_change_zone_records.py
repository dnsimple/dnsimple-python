import json
from dataclasses import dataclass
from typing import List, Optional

import omitempty

from dnsimple.struct import Struct
from dnsimple.struct.zone_record import ZoneRecord


@dataclass
class BatchChangeZoneRecordsCreateInput(dict):
    """Represents a zone record creation input for batch change"""

    def __init__(self, name: str, type: str, content: str, ttl: Optional[int] = None, priority: Optional[int] = None, regions: Optional[List[str]] = None):
        dict.__init__(self, name=name, type=type, content=content, ttl=ttl, priority=priority, regions=regions)


@dataclass
class BatchChangeZoneRecordsUpdateInput(dict):
    """Represents a zone record update input for batch change"""

    def __init__(self, id: int, name: Optional[str] = None, content: Optional[str] = None, ttl: Optional[int] = None, priority: Optional[int] = None, regions: Optional[List[str]] = None):
        dict.__init__(self, id=id, name=name, content=content, ttl=ttl, priority=priority, regions=regions)


@dataclass
class BatchChangeZoneRecordsDeleteInput(dict):
    """Represents a zone record deletion input for batch change"""

    def __init__(self, id: int):
        dict.__init__(self, id=id)


@dataclass
class BatchChangeZoneRecordsInput(dict):
    """Represents the data to send to the DNSimple API to batch change zone records"""

    def __init__(self, creates: Optional[List[BatchChangeZoneRecordsCreateInput]] = None,
                 updates: Optional[List[BatchChangeZoneRecordsUpdateInput]] = None,
                 deletes: Optional[List[BatchChangeZoneRecordsDeleteInput]] = None):
        data = {}
        if creates is not None:
            data['creates'] = creates
        if updates is not None:
            data['updates'] = updates
        if deletes is not None:
            data['deletes'] = deletes
        dict.__init__(self, **data)

    def to_json(self):
        return json.dumps(omitempty(self))


@dataclass
class BatchChangeZoneRecordsDeleteResponse(Struct):
    """Represents a deleted zone record in the batch change response"""
    id = None
    """The record ID that was deleted"""

    def __init__(self, data):
        super().__init__(data)


@dataclass
class BatchChangeZoneRecordsResponse(Struct):
    """Represents the response from batch changing zone records"""
    creates = None
    """List of created zone records"""
    updates = None
    """List of updated zone records"""
    deletes = None
    """List of deleted zone record IDs"""

    def __init__(self, data):
        super().__init__(data)
        if 'creates' in data and data['creates'] is not None:
            self.creates = [ZoneRecord(item) for item in data['creates']]
        if 'updates' in data and data['updates'] is not None:
            self.updates = [ZoneRecord(item) for item in data['updates']]
        if 'deletes' in data and data['deletes'] is not None:
            self.deletes = [BatchChangeZoneRecordsDeleteResponse(item) for item in data['deletes']]