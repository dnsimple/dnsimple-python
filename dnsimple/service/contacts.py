from dnsimple.response import Response
from dnsimple.struct import Contact


class Contacts(object):
    """
    Handles communication with the contact related methods of the DNSimple API.

    See https://developer.dnsimple.com/v2/contacts/
    """

    def __init__(self, client):
        self.client = client

    def list_contacts(self, account_id, page=None, per_page=None):
        """
        Lists the contacts in the account

        See https://developer.dnsimple.com/v2/contacts/#listContacts

        :param account_id: int
            The account id
        :param page: int
            The page to return (default: 1)
        :param per_page: int
            The number of entries to return per page (default: 30, maximum: 100)

        :return: dnsimple.Response
            The list of contacts
        """
        response = self.client.get(f'/{account_id}/contacts', page=page, per_page=per_page)
        return Response(response, Contact)

    def create_contact(self, account_id, contact):
        """
        Creates a new contact in the account

        See https://developer.dnsimple.com/v2/contacts/#createContact
        
        :param account_id: int
            The account id
        :param contact: dnsimple.struct.Contact
            The contact to be created

        :return: dnsimple.Response
            The newly created contact
        """
        response = self.client.post(f'/{account_id}/contacts', data=contact.to_json())
        return Response(response, Contact)

    def get_contact(self, account_id, contact_id):
        """
        Gets a contact from the account

        See https://developer.dnsimple.com/v2/contacts/#getContact

        :param account_id: int
            Then account id
        :param contact_id: int
            The contact id

        :return: dnsimple.Response
            The contact
        """
        response = self.client.get(f'/{account_id}/contacts/{contact_id}')
        return Response(response, Contact)

    def update_contact(self, account_id, contact_id, contact):
        """
        Updates a contact in the account

        See https://developer.dnsimple.com/v2/contacts/#updateContact

        :param account_id: int
            The account id
        :param contact_id: int
            The contact id
        :param contact: dnsimple.struct.Contact
            The contact attributes to be updated

        :return: dnsimple.Response
            The updated contact
        """
        response = self.client.patch(f'/{account_id}/contacts/{contact_id}', data=contact.to_json())
        return Response(response, Contact)

    def delete_contact(self, account_id, contact_id):
        """
        Deletes a contact from the account

        See https://developer.dnsimple.com/v2/contacts/#deleteContact

        :param account_id: int
            The account id
        :param contact_id: int
            The contact id

        :return: dnsimple.Response
            An empty response
        """
        response = self.client.delete(f'/{account_id}/contacts/{contact_id}')
        return Response(response)
