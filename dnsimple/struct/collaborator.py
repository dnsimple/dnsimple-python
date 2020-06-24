from dataclasses import dataclass

from dnsimple.struct import Struct


@dataclass
class Collaborator(Struct):
    """
    Represents a collaborator for a domain in the account

    See: https://developer.dnsimple.com/v2/domains/collaborators/
    """

    id = None
    """The collaborator ID in DNSimple"""
    domain_id = None
    """The associated domain ID"""
    domain_name = None
    """The associated domain name"""
    user_id = None
    """The user ID (if the collaborator accepted the invitation)."""
    user_email = None
    """The user email"""
    invitation = None
    """Invitation"""
    created_at = None
    """When the collaborator was created in DNSimple"""
    updated_at = None
    """When the collaborator was last updated in DNSimple"""
    accepted_at = None
    """When the collaborator accepted the invitation"""

    def __init__(self, data):
        super().__init__(data)
