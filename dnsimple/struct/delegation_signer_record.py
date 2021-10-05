import json
from dataclasses import dataclass

import omitempty

from dnsimple.struct import Struct


@dataclass
class DelegationSignerRecord(Struct):
    """Represents a delegation signer record"""

    id = None
    """The ID of the delegation signer record in DNSimple."""
    domain_id = None
    """The associated domain ID."""
    algorithm = None
    """The signing algorithm used."""
    digest = None
    """The digest value."""
    digest_type = None
    """The digest type used."""
    keytag = None
    """The keytag for the associated DNSKEY."""
    public_key = None
    """The public key that references the corresponding DNSKEY record."""
    created_at = None
    """When the delegation signing record was created in DNSimple."""
    updated_at = None
    """When the delegation signing record was last updated in DNSimple."""

    def __init__(self, data):
        super().__init__(data)


@dataclass
class DelegationSignerRecordInput(dict):
    """Represents the input we send to create a domain delegation signer record"""

    def __init__(self, algorithm, digest=None, digest_type=None, keytag=None, public_key=None):
        """
        :param algorithm: str
            Required DNSSEC algorithms defined in
            http://www.iana.org/assignments/dns-sec-alg-numbers/dns-sec-alg-numbers.xhtml
            - pass the Number value as a string (i.e. '8').
        :param digest: str
            Required if TLD requires DS data.
            The hexadecimal representation of the digest of the corresponding DNSKEY record.
        :param digest_type: str
            Required if TLD requires DS data.
            DNSSEC digest types defined in http://www.iana.org/assignments/ds-rr-types/ds-rr-types.xhtml
            - pass the Number value as string (i.e. '2').
        :param keytag: str
            Required if TLD requires DS data.
            A keytag that references the corresponding DNSKEY record.
        :param public_key: str
            Required if TLD requires KEY data.
            The public key that references the corresponding DNSKEY record.
        """
        dict.__init__(self, algorithm=algorithm, digest=digest, digest_type=digest_type, keytag=keytag, public_key=public_key)

    def to_json(self):
        return json.dumps(omitempty(self))
