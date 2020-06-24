import unittest

import responses

from dnsimple import DNSimpleException
from dnsimple.response import Pagination
from dnsimple.struct import Contact
from tests.helpers import DNSimpleMockResponse, DNSimpleTest


class ContactsTest(DNSimpleTest):
    @responses.activate
    def test_list_contacts(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/contacts',
                                           fixture_name='listContacts/success'))
        contacts = self.contacts.list_contacts(1010).data

        self.assertEqual(2, len(contacts))
        self.assertIsInstance(contacts[0], Contact)

    @responses.activate
    def test_list_contacts_supports_pagination(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/contacts?page=1&per_page=2',
                                           fixture_name='listContacts/success'))
        response = self.contacts.list_contacts(1010, page=1, per_page=2)

        self.assertIsInstance(response.pagination, Pagination)

    @responses.activate
    def test_create_contact(self):
        responses.add(DNSimpleMockResponse(method=responses.POST,
                                           path='/1010/contacts',
                                           fixture_name='createContact/created'))
        contact = Contact.new(label='Default', first_name='First', last_name='User', job_title='CEO',
                              organization_name='Awesome Company', email='first@example.com', phone='+18001234567',
                              fax='+18011234567', address1='Italian Street, 10', address2='', city='Roma',
                              state_province='RM', postal_code='00100', country='IT')
        created = self.contacts.create_contact(1010, contact).data

        self.assertEqual(contact.label, created.label)
        self.assertEqual(contact.first_name, created.first_name)
        self.assertEqual(contact.last_name, created.last_name)
        self.assertEqual(contact.job_title, created.job_title)
        self.assertEqual(contact.organization_name, created.organization_name)
        self.assertEqual(contact.email, created.email)
        self.assertEqual(contact.phone, created.phone)
        self.assertEqual(contact.fax, created.fax)
        self.assertEqual(contact.address1, created.address1)
        self.assertEqual(contact.address2, created.address2)
        self.assertEqual(contact.city, created.city)
        self.assertEqual(contact.state_province, created.state_province)
        self.assertEqual(contact.postal_code, created.postal_code)
        self.assertEqual(contact.country, created.country)

    @responses.activate
    def test_get_contact(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/contacts/1',
                                           fixture_name='getContact/success'))
        contact = self.contacts.get_contact(1010, 1).data

        self.assertIsInstance(contact, Contact)

    @responses.activate
    def test_update_contact(self):
        responses.add(DNSimpleMockResponse(method=responses.PATCH,
                                           path='/1010/contacts/1',
                                           fixture_name='updateContact/success'))
        contact = Contact.new(label='Default')

        updated = self.contacts.update_contact(1010, 1, contact).data

        self.assertEqual(contact.label, updated.label)

    @responses.activate
    def test_delete_contact(self):
        responses.add(DNSimpleMockResponse(method=responses.DELETE,
                                           path='/1010/contacts/1',
                                           fixture_name='deleteContact/success'))
        self.contacts.delete_contact(1010, 1)

    @responses.activate
    def test_delete_contact_in_use(self):
        responses.add(DNSimpleMockResponse(method=responses.DELETE,
                                           path='/1010/contacts/1',
                                           fixture_name='deleteContact/error-contact-in-use'))
        try:
            self.contacts.delete_contact(1010, 1)
        except DNSimpleException as dnse:
            self.assertEqual("The contact cannot be deleted because it's currently in use", dnse.message)


if __name__ == '__main__':
    unittest.main()
