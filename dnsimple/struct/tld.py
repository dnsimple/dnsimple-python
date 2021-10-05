from dataclasses import dataclass

from dnsimple.struct import Struct


@dataclass
class Tld(Struct):
    """Represents a TLD in DNSimple"""

    tld = None
    """The TLD in DNSimple"""
    tld_type = None
    """The TLD type"""
    whois_privacy = None
    """True if Whois Privacy Protection is available"""
    auto_renew_only = None
    """True if TLD requires use of auto-renewal for renewals"""
    idn = None
    """True if IDN is available"""
    minimum_registration = None
    """The minimum registration period, in years"""
    registration_enabled = None
    """True if DNSimple supports registrations for this TLD"""
    renewal_enabled = None
    """True if DNSimple supports renewals for this TLD"""
    transfer_enabled = None
    """True if DNSimple supports inbound transfers for this TLD"""
    dnssec_interface_type = None
    """Type of data interface required for DNSSEC for this TLD"""

    def __init__(self, data):
        super().__init__(data)


@dataclass
class TldExtendedAttributeOption(Struct):
    """Represents a single option you can assign to an extended attributes."""

    title = None
    """The option name"""
    value = None
    """The option value"""
    description = None
    """A long description of the option"""

    def __init__(self, data):
        super().__init__(data)


@dataclass
class TldExtendedAttribute(Struct):
    """Represents an extended attributes supported or required by a specific TLD."""

    name = None
    """The extended attribute name"""
    description = None
    """A description of the extended attribute"""
    required = None
    """Boolean indicating if the extended attribute is required"""
    options = None
    """The list of options with possible values for the extended attribute"""

    def __init__(self, data):
        super().__init__(data)
        self.options = list(map(TldExtendedAttributeOption, self.options))
