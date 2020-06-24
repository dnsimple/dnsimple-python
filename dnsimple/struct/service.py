from dataclasses import dataclass

from dnsimple.struct import Struct


@dataclass
class Service(Struct):
    """Represents a Service in DNSimple"""

    id = None
    """The service ID in DNSimple"""
    name = None
    """The service name"""
    sid = None
    """A string ID for the service"""
    description = None
    """The service description"""
    setup_description = None
    """The service setup description"""
    requires_setup = None
    """Whether the service requires extra setup"""
    default_subdomain = None
    """The default subdomain where the service will be applied"""
    created_at = None
    """When the service was created in DNSimple"""
    updated_at = None
    """When the service was last updated in DNSimple"""
    settings = None
    """The array of settings to setup this service, if setup is required."""

    def __init__(self, data):
        super().__init__(data)
        self.settings = list(map(ServiceSetting, self.settings))


@dataclass
class ServiceSetting(Struct):
    """Represents a single group of settings for a DNSimple Service"""

    name = None
    """The setting name"""
    label = None
    """The setting label"""
    append = None
    """A suffix to be appended to the setting value"""
    description = None
    """The setting description"""
    example = None
    """An example of the setting value"""
    password = None
    """Whether the setting requires a password"""
    def __init__(self, data):
        super().__init__(data)
