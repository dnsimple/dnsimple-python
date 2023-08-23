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


class Identity(object):
    def __init__(self, client):
        self.client = client

    def whoami(self):
        """
        Retrieves the details about the current authenticated entity used to access the API.

        See https://developer.dnsimple.com/v2/identity/#whoami

        """
        response = self.client.get(f"/whoami")
        return Response(response, types.WhoamiOutput)
