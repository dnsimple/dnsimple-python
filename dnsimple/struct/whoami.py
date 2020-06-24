from dataclasses import dataclass

from dnsimple.struct.account import Account
from dnsimple.struct.user import User


@dataclass
class Whoami(object):
    """
    Represents the structure holding a User and Account object.
    """
    account = None
    """The account, if present"""
    user = None
    """The user, if present"""

    def __init__(self, data):
        self.account = None if data['account'] is None else Account(data['account'])
        self.user = None if data['user'] is None else User(data['user'])
