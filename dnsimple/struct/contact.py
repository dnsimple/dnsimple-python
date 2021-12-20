import json
from dataclasses import dataclass

import omitempty

from dnsimple.extra import attach_attributes_to


@dataclass
class Contact(dict):
    id = None
    """The contact ID in DNSimple"""
    account_id = None
    """The associated account ID"""
    label = None
    """The label to represent the contact"""
    first_name = None
    """The contact first name"""
    last_name = None
    """The contact last name"""
    job_title = None
    """The contact's job title"""
    organization_name = None
    """The name of the organization in which the contact works"""
    address1 = None
    """The contact street address"""
    address2 = None
    """Apartment or suite number"""
    city = None
    """The city name"""
    state_province = None
    """The state or province name"""
    postal_code = None
    """The contact postal code"""
    country = None
    """The contact country (as a 2-character country code)"""
    phone = None
    """The contact phone number"""
    fax = None
    """The contact fax number (may be omitted)"""
    email = None
    """The contact email address"""
    created_at = None
    """When the contact was created in DNSimple"""
    updated_at = None
    """When the contact was last updated in DNSimple"""

    def __init__(self, data):
        attach_attributes_to(self, data)
        dict.__init__(self, label=self.label, first_name=self.first_name, last_name=self.last_name,
                      job_title=self.job_title, organization_name=self.organization_name, email=self.email,
                      phone=self.phone, fax=self.fax, address1=self.address1, address2=self.address2, city=self.city,
                      state_province=self.state_province, postal_code=self.postal_code, country=self.country)

    def to_json(self):
        return json.dumps(omitempty(self))

    @classmethod
    def new(cls, label=None, first_name=None, last_name=None, job_title=None, organization_name=None, email=None,
            phone=None, fax=None, address1=None, address2=None, city=None, state_province=None, postal_code=None,
            country=None):
        """
        Creates a new instance a contact.

        :param label: str
        :param first_name: str
        :param last_name: st
        :param job_title: str
        :param organization_name: str
        :param email: str
        :param phone: str
        :param fax: str
        :param address1: str
        :param address2: str
        :param city: str
        :param state_province: str
        :param postal_code: str
        :param country: str

        :return: Contact
        """
        return cls({'label': label, 'first_name': first_name, 'last_name': last_name, 'job_title': job_title,
                    'organization_name': organization_name, 'email': email, 'phone': phone, 'fax': fax,
                    'address1': address1, 'address2': address2, 'city': city, 'state_province': state_province,
                    'postal_code': postal_code, 'country': country})
