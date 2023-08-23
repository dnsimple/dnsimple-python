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


class Templates(object):
    def __init__(self, client):
        self.client = client

    def list_templates(self, account: int, *, sort=None):
        """
        Lists the templates in the account.

        See https://developer.dnsimple.com/v2/templates/#listTemplates

        :param account:
            The account id
        """
        response = self.client.get(f"/{account}/templates")
        return Response(response, types.Template)

    def create_template(self, account: int, input: types.CreateTemplateInput):
        """
        Creates a template.

        See https://developer.dnsimple.com/v2/templates/#createTemplate

        :param account:
            The account id
        """
        response = self.client.post(f"/{account}/templates")
        return Response(response, types.Template)

    def get_template(self, account: int, template: str):
        """
        Retrieves the details of an existing template.

        See https://developer.dnsimple.com/v2/templates/#getTemplate

        :param account:
            The account id
        :param template:
            The template id or short name
        """
        response = self.client.get(f"/{account}/templates/{template}")
        return Response(response, types.Template)

    def update_template(
        self, account: int, template: str, input: types.UpdateTemplateInput
    ):
        """
        Updates the template details.

        See https://developer.dnsimple.com/v2/templates/#updateTemplate

        :param account:
            The account id
        :param template:
            The template id or short name
        """
        response = self.client.patch(f"/{account}/templates/{template}")
        return Response(response, types.Template)

    def delete_template(self, account: int, template: str):
        """
        Permanently deletes a template.

        See https://developer.dnsimple.com/v2/templates/#deleteTemplate

        :param account:
            The account id
        :param template:
            The template id or short name
        """
        response = self.client.delete(f"/{account}/templates/{template}")
        return Response(
            response,
        )

    def list_template_records(self, account: int, template: str, *, sort=None):
        """
        Lists the records for a template.

        See https://developer.dnsimple.com/v2/templates/#listTemplateRecords

        :param account:
            The account id
        :param template:
            The template id or short name
        """
        response = self.client.get(f"/{account}/templates/{template}/records")
        return Response(response, types.TemplateRecord)

    def create_template_record(
        self, account: int, template: str, input: types.CreateTemplateRecordInput
    ):
        """
        Creates a new template record.

        See https://developer.dnsimple.com/v2/templates/#createTemplateRecord

        :param account:
            The account id
        :param template:
            The template id or short name
        """
        response = self.client.post(f"/{account}/templates/{template}/records")
        return Response(response, types.TemplateRecord)

    def get_template_record(self, account: int, template: str, templaterecord: int):
        """
        Retrieves the details of an existing template record.

        See https://developer.dnsimple.com/v2/templates/#getTemplateRecord

        :param account:
            The account id
        :param template:
            The template id or short name
        :param templaterecord:
            The template record id
        """
        response = self.client.get(
            f"/{account}/templates/{template}/records/{templaterecord}"
        )
        return Response(response, types.TemplateRecord)

    def delete_template_record(self, account: int, template: str, templaterecord: int):
        """
        Permanently deletes a template record.

        See https://developer.dnsimple.com/v2/templates/#deleteTemplateRecord

        :param account:
            The account id
        :param template:
            The template id or short name
        :param templaterecord:
            The template record id
        """
        response = self.client.delete(
            f"/{account}/templates/{template}/records/{templaterecord}"
        )
        return Response(
            response,
        )

    def apply_template(self, account: int, domain: str, template: str):
        """
        Applies a template to a domain.

        See https://developer.dnsimple.com/v2/templates/#applyTemplateToDomain

        :param account:
            The account id
        :param domain:
            The domain name or id
        :param template:
            The template id or short name
        """
        response = self.client.post(f"/{account}/domains/{domain}/templates/{template}")
        return Response(
            response,
        )
