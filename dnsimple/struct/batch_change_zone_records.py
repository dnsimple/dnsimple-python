import json
from dataclasses import dataclass

import omitempty

from dnsimple.struct import Struct
from dnsimple.struct.zone_record import ZoneRecord


@dataclass
class BatchChangeZoneRecordsUpdateInput(dict):
    """Represents a zone record update input for a batch operation"""

    def __init__(self, id, name=None, content=None, ttl=None, priority=None, regions=None):
        dict.__init__(self, id=id, name=name, content=content, ttl=ttl, priority=priority, regions=regions)

    def to_json(self):
        omitted = omitempty(self)

        if self['name'] == '':
            omitted['name'] = ''

        return json.dumps(omitted)


@dataclass
class BatchChangeZoneRecordsDeleteInput(dict):
    """Represents a zone record deletion input for a batch operation"""

    def __init__(self, id):
        dict.__init__(self, id=id)


@dataclass
class BatchChangeZoneRecordsInput(dict):
    """Represents the data to send to the DNSimple API to make a batch change on the records of a zone

    All parameters are optional - you can perform creates only, updates only, deletes only,
    or any combination of the three operations.

    :param creates: List[ZoneRecordInput] - Records to create (optional)
    :param updates: List[BatchChangeZoneRecordsUpdateInput] - Records to update (optional)
    :param deletes: List[BatchChangeZoneRecordsDeleteInput] - Records to delete (optional)
    """

    def __init__(self, creates=None, updates=None, deletes=None):
        data = {}
        if creates is not None:
            data['creates'] = creates
        if updates is not None:
            data['updates'] = updates
        if deletes is not None:
            data['deletes'] = deletes
        dict.__init__(self, **data)

    def to_json(self):
        result = {}

        if 'creates' in self and self['creates'] is not None:
            result['creates'] = [json.loads(item.to_json()) for item in self['creates']]

        if 'updates' in self and self['updates'] is not None:
            result['updates'] = [json.loads(item.to_json()) for item in self['updates']]

        if 'deletes' in self and self['deletes'] is not None:
            result['deletes'] = [omitempty(item) for item in self['deletes']]

        return json.dumps(result)


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
