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


class Contacts(object):
    def __init__(self, client):
        self.client = client

    def list_contacts(self, account: int, *, sort=None):
        """
        List contacts in the account.

        See https://developer.dnsimple.com/v2/contacts/#listContacts

        :param account:
            The account id
        """
        response = self.client.get(f"/{account}/contacts")
        return Response(response, types.Contact)

    def create_contact(self, account: int, input: types.CreateContactInput):
        """
        Creates a contact.

        See https://developer.dnsimple.com/v2/contacts/#createContact

        :param account:
            The account id
        """
        response = self.client.post(f"/{account}/contacts")
        return Response(response, types.Contact)

    def get_contact(self, account: int, contact: int):
        """
        Retrieves the details of an existing contact.

        See https://developer.dnsimple.com/v2/contacts/#getContact

        :param account:
            The account id
        :param contact:
            The contact id
        """
        response = self.client.get(f"/{account}/contacts/{contact}")
        return Response(response, types.Contact)

    def update_contact(
        self, account: int, contact: int, input: types.UpdateContactInput
    ):
        """
        Updates the contact details.

        See https://developer.dnsimple.com/v2/contacts/#updateContact

        :param account:
            The account id
        :param contact:
            The contact id
        """
        response = self.client.patch(f"/{account}/contacts/{contact}")
        return Response(response, types.Contact)

    def delete_contact(self, account: int, contact: int):
        """
        Permanently deletes a contact from the account.

        See https://developer.dnsimple.com/v2/contacts/#deleteContact

        :param account:
            The account id
        :param contact:
            The contact id
        """
        response = self.client.delete(f"/{account}/contacts/{contact}")
        return Response(
            response,
        )
