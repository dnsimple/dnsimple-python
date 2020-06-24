from dnsimple.response import Response
from dnsimple.struct import Template, TemplateRecord


class Templates(object):
    def __init__(self, client):
        self.client = client

    def list_templates(self, account_id, sort=None, page=None, per_page=None):
        """
        Lists the templates in the account

        See https://developer.dnsimple.com/v2/templates/#listTemplates

        :param account_id: int
            The account id
        :param sort: str
            Comma separated key-value pairs: the name of a field and the order criteria (asc for ascending and desc for
            descending).

            Possible sort criteria:
                - id: Sort templates by ID (i.e. 'id:asc')
                - name: Sort templates by name (alphabetical order) (i.e. 'name:desc')
                - sid: Sort templates by sid (i.e. 'sid:asc')
        :param page: int
            The page to return (default: 1)
        :param per_page: int
            The number of entries to return per page (default: 30, maximum: 100)

        :return: dnsimple.Response
            The templates in the account
        """
        response = self.client.get(f'/{account_id}/templates', sort=sort, page=page, per_page=per_page)
        return Response(response, Template)

    def create_template(self, account_id, template_attributes):
        """
        Creates a template in the account

        See https://developer.dnsimple.com/v2/templates/#createTemplate

        :param account_id: int
            The account id
        :param template_attributes: dnsimple.struct.Template
            The template attributes
        :return: dnsimple.Response
            The newly created template
        """
        response = self.client.post(f'/{account_id}/templates', data=template_attributes.to_json())
        return Response(response, Template)

    def get_template(self, account_id, template):
        """
        Gets the template with the specified id or sid

        See https://developer.dnsimple.com/v2/templates/#getTemplate

        :param account_id: int
            The account id
        :param template: int/str
            The template sid or id

        :return: dnsimple.Response
            The template requested
        """
        response = self.client.get(f'/{account_id}/templates/{template}')
        return Response(response, Template)

    def update_template(self, account_id, template, template_attributes):
        """
        Updates a template with the provided data

        See https://developer.dnsimple.com/v2/templates/#updateTemplate

        :param account_id: int
            The account id
        :param template: int/str
            The template id or sid
        :param template_attributes: dnsimple.struct.Template
            The template attributes to update the template with

        :return: dnsimple.Response
            The updated template
        """
        response = self.client.patch(f'/{account_id}/templates/{template}', data=template_attributes.to_json())
        return Response(response, Template)

    def delete_template(self, account_id, template):
        """
        Deletes a template from the account

        WARNING: This cannot be undone

        See https://developer.dnsimple.com/v2/templates/#deleteTemplate

        :param account_id: int
            The account id
        :param template: int/str
            The template id or sid

        :return: dnsimple.Response
            An empty response
        """
        response = self.client.delete(f'/{account_id}/templates/{template}')
        return Response(response)

    def list_template_records(self, account_id, template, sort=None, page=None, per_page=None):
        """
        Lists the records in the template

        See https://developer.dnsimple.com/v2/templates/records/#listTemplateRecords

        :param account_id: int
            The account id
        :param template: int/str
            The template id or sid
        :param sort: str
            Comma separated key-value pairs: the name of a field and the order criteria (asc for ascending and desc for
            descending).

            Possible sort criteria:
                - id: Sort template records by ID (i.e. 'id:asc')
                - name: Sort template records by name (i.e. 'name:desc')
                - content: Sort template records by content (i.e. 'content:asc')
                - type: Sort template records by type (i.e. 'type:desc')
        :param page: int
            The page to return (default: 1)
        :param per_page: int
            The number of entries to return per page (default: 30, maximum: 100)

        :return: dnsimple.Response
            The list of template records
        """
        response = self.client.get(f'/{account_id}/templates/{template}/records', sort=sort, page=page, per_page=per_page)
        return Response(response, TemplateRecord)

    def create_template_record(self, account_id, template, template_record_attributes):
        """
        Creates a record in the template

        See https://developer.dnsimple.com/v2/templates/records/#createTemplateRecord

        :param account_id: int
            The account id
        :param template: int/str
            The template id or sid
        :param template_record_attributes: dnsimple.struct.TemplateRecord
            The template record attributes

        :return: dnsimple.Response
            The newly created template record
        """
        response = self.client.post(f'/{account_id}/templates/{template}/records', data=template_record_attributes.to_json())
        return Response(response, TemplateRecord)

    def get_template_record(self, account_id, template, record_id):
        """
        Gets a record from the template

        See https://developer.dnsimple.com/v2/templates/records/#getTemplateRecord

        :param account_id: int
            The account id
        :param template: int/str
            The template id or sid
        :param record_id: int
            The template record id

        :return: dnsimple.Response
            The template record
        """
        response = self.client.get(f'/{account_id}/templates/{template}/records/{record_id}')
        return Response(response, TemplateRecord)

    def delete_template_record(self, account_id, template, record_id):
        """
        Deletes a record from the template.

        WARNING: this cannot be undone.

        See https://developer.dnsimple.com/v2/templates/records/#deleteTemplateRecord

        :param account_id: int
            The account id
        :param template: int/str
            The template id or sid
        :param record_id: int
            The template record id

        :return: dnsimple.Response
            An empty response
        """
        response = self.client.delete(f'/{account_id}/templates/{template}/records/{record_id}')
        return Response(response)

    def apply_template(self, account_id, domain, template):
        """
        Applies a template to the domain

        See https://developer.dnsimple.com/v2/templates/domains/#applyTemplateToDomain

        :param account_id: int
            The account id
        :param domain: int/str
            The domain name or id
        :param template: int/str
            The template id or sid

        :return: dnsimple.Response
            An empty response
        """
        response = self.client.post(f'/{account_id}/domains/{domain}/templates/{template}')
        return Response(response)
