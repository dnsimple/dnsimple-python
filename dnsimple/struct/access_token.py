from dataclasses import dataclass

from dnsimple.struct import Struct


@dataclass
class AccessToken(Struct):
    """
    AccessToken represents a DNSimple Oauth access token.

    See https://developer.dnsimple.com/v2/oauth/
    """

    account_id = None
    """The account ID in DNSimple this token belongs to."""
    token_type = None
    """The token type."""
    access_token = None
    """The token you can use to authenticate."""
    scope = None
    """The token scope (not used for now)."""

    def __init__(self, data):
        super().__init__(data)
