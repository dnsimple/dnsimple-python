import json
from dataclasses import dataclass

import omitempty

from dnsimple.struct import Struct


@dataclass
class ZoneRecordUpdateInput(dict):
    """Represents the data to send tot the DNSimple API to update a zone record"""

    def __init__(self, name=None, content=None, ttl=None, priority=None, regions=None):
        dict.__init__(self, name=name, content=content, ttl=ttl, priority=priority, regions=regions)

    def to_json(self):
        return json.dumps(omitempty(self))


@dataclass
class ZoneRecordInput(dict):
    """Represents the data to send to the DNSimple API to create a zone record"""

    def __init__(self, name, type, content, ttl=None, priority=None, regions=None):
        dict.__init__(self, name=name, type=type, content=content, ttl=ttl, priority=priority, regions=regions)

    def to_json(self):
        return json.dumps(omitempty(self))


@dataclass
class ZoneRecord(Struct):
    """Represents a zone record"""
    id = None
    """The record ID in DNSimple"""
    zone_id = None
    """The associated zone ID in DNSimple"""
    parent_id = None
    """The ID of the parent record, if this record is dependent on another record."""
    type = None
    """The type of record, in uppercase."""
    name = None
    """The record name (without the domain name)."""
    content = None
    """The plain-text record content"""
    ttl = None
    """The TTL value"""
    priority = None
    """The priority value, if the type of record accepts a priority."""
    regions = None
    """The regions where the record is propagated. This is optional."""
    system_record = None
    """True if this is a system record created by DNSimple. System records are read-only."""
    created_at = None
    """When the record was created in DNSimple."""
    updated_at = None
    """When the record was last updated in DNSimple."""

    def __init__(self, data):
        super().__init__(data)
