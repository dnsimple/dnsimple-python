from dataclasses import dataclass

from dnsimple.extra import attach_attributes_to


@dataclass
class Struct(object):

    def __init__(self, data):
        attach_attributes_to(self, data)
