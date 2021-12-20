import json
from dataclasses import dataclass

import omitempty

from dnsimple.extra import attach_attributes_to


@dataclass
class TemplateRecord(dict):
    """Represents a DNS record for a template in DNSimple"""

    id = None
    """The template record ID in DNSimple"""
    template_id = None
    """The template ID in DNSimple"""
    name = None
    """The template record name (without the domain name)"""
    content = None
    """The plain-text template record content"""
    ttl = None
    """The template record TTL value"""
    type = None
    """The type of template record, in uppercase"""
    priority = None
    """The priority value, if the type of template record accepts a priority"""
    created_at = None
    """When the template record was created in DNSimple"""
    updated_at = None
    """When the template record was last updated in DNSimple"""

    def __init__(self, data):
        attach_attributes_to(self, data)
        dict.__init__(self, id=self.id, template_id=self.template_id, name=self.name, content=self.content,
                      ttl=self.ttl, type=self.type, priority=self.priority, created_at=self.created_at,
                      updated_at=self.updated_at)

    def to_json(self):
        return json.dumps(omitempty(self))

    @classmethod
    def new(cls, name, type, content, ttl=None, priority=None):
        """
        Creates a new template record

        :param name: str
        :param type: str
        :param content: str
        :param ttl: int
        :param priority: int
        :return: TemplateRecord
        """
        return cls({'name': name, 'type': type, 'content': content, 'ttl': ttl, 'priority': priority})
