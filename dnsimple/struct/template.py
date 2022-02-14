import json
from dataclasses import dataclass

import omitempty

from dnsimple.extra import attach_attributes_to


@dataclass
class Template(dict):
    """Represents a template in DNSimple"""

    id = None
    """The template ID in DNSimple"""
    account_id = None
    """The associated account ID"""
    name = None
    """The template name"""
    sid = None
    """The string ID for the template"""
    description = None
    """The template description"""
    created_at = None
    """When the template was created in DNSimple"""
    updated_at = None
    """When the template was last updated in DNSimple"""

    def __init__(self, data):
        attach_attributes_to(self, data)
        dict.__init__(self, id=self.id, account_id=self.account_id, name=self.name, sid=self.sid,
                      description=self.description, created_at=self.created_at, updated_at=self.updated_at)

    def to_json(self):
        return json.dumps(omitempty(self))

    @classmethod
    def new(cls, name, sid, description):
        """
        Creates a new template

        :param name: str
        :param sid: str
        :param description: str
        :return: Template
            The newly created template
        """
        return cls({'name': name, 'sid': sid, 'description': description})
