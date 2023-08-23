from dataclasses import dataclass
from dataclasses import field
from dataclasses_json import config
from dataclasses_json import dataclass_json
from dnsimple.response import Response
from typing import Any
from typing import Dict
from typing import List
from typing import Literal
from typing import Union
import dnsimple.struct as types


class Accounts(object):
    def __init__(self, client):
        self.client = client

    def list_accounts(self):
        """
        Lists the accounts the current authenticated entity has access to.

        See https://developer.dnsimple.com/v2/accounts/#listAccounts

        """
        response = self.client.get(f"/accounts")
        return Response(response, types.Account)
