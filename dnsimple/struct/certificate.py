import json
from dataclasses import dataclass

import omitempty
import warnings

from dnsimple.struct import Struct


@dataclass
class Certificate(Struct):
    """Represents a Certificate in DNSimple"""

    id = None
    """The certificate ID in DNSimple"""
    domain_id = None
    """The associated domain ID"""
    contact_id = None
    """The associated contact ID"""
    name = None
    """The certificate name"""
    common_name = None
    """The certificate common name"""
    years = None
    """The years the certificate will last"""
    csr = None
    """The certificate CSR"""
    state = None
    """The certificate state"""
    auto_renew = False
    """True if the certificate is set to auto-renew on expiration"""
    alternate_names = None
    """The certificate alternate names"""
    authority_identifier = None
    """The Certificate Authority (CA) that issued the certificate"""
    created_at = None
    """When the certificate was created in DNSimple"""
    updated_at = None
    """When the certificate was last updated in DNSimple"""
    expires_on = None
    """When the certificate will expire"""

    def __init__(self, data):
        super().__init__(data)


@dataclass
class CertificateBundle(Struct):
    """Represents a certificate download in DNSimple"""
    server = None
    """The server certificate"""
    root = None
    """The root certificate"""
    chain = None
    """The intermediate certificates"""
    private_key = None
    """The certificate private key"""

    def __init__(self, data):
        super().__init__(data)


class LetsencryptCertificateInput(dict):
    def __init__(self, contact_id=None, auto_renew=None, name=None, alternate_names=None, signature_algorithm=None):
        dict.__init__(self, auto_renew=auto_renew, name=name, alternate_names=alternate_names, signature_algorithm=signature_algorithm)
        if contact_id is not None:
            warnings.warn("DEPRECATION WARNING: LetsencryptCertificateInput#contact_id is deprecated and its value is ignored and will be removed in the next major version.")


    def to_json(self):
        return json.dumps(omitempty(self))


class LetsencryptCertificateRenewalInput(dict):
    def __init__(self, auto_renew=None, signature_algorithm=None):
        dict.__init__(self, auto_renew=auto_renew, signature_algorithm=signature_algorithm)


    def to_json(self):
        return json.dumps(omitempty(self))


@dataclass
class CertificatePurchase(Struct):
    """Represents a certificate purchase in DNSimple"""
    id = None
    """The certificate purchase ID in DNSimple"""
    certificate_id = None
    """The certificate ID"""
    state = None
    """The certificate renewal state"""
    auto_renew = None
    """True if the certificate is requested to auto-renew"""
    created_at = None
    """When the certificate renewal was created in DNSimple"""
    updated_at = None
    """When the certificate renewal was last updated in DNSimple"""

    def __init__(self, data):
        super().__init__(data)


@dataclass
class CertificateRenewal(Struct):
    """Represents a Certificate Renewal in DNSimple"""

    id = None
    """The certificate renewal ID in DNSimple"""
    old_certificate_id = None
    """The old certificate ID"""
    new_certificate_id = None
    """The new certificate ID"""
    state = None
    """The certificate renewal state"""
    auto_renew = None
    """True if the certificate is requested to auto-renew"""
    created_at = None
    """When the certificate renewal was created in DNSimple"""
    updated_at = None
    """When the certificate renewal was last updated in DNSimple"""

    def __init__(self, data):
        super().__init__(data)
