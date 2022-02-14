import json
from dataclasses import dataclass

import omitempty

from dnsimple.extra import attach_attributes_to


@dataclass
class Webhook(dict):
    """Represents a DNSimple webhook"""

    id = None
    """The contact ID in DNSimple"""
    url = None
    """The callback URL"""

    def __init__(self, data):
        attach_attributes_to(self, data)
        dict.__init__(self, id=self.id, url=self.url)

    def to_json(self):
        return json.dumps(omitempty(self))

    @classmethod
    def new(cls, url):
        return cls({'url': url})
