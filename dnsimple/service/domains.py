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


class Domains(object):
    def __init__(self, client):
        self.client = client

    def list_domains(
        self, account: int, *, name_like=None, registrant_id=None, sort=None
    ):
        """
        Lists the domains in the account.

        See https://developer.dnsimple.com/v2/domains/#listDomains

        :param account:
            The account id
        """
        response = self.client.get(f"/{account}/domains")
        return Response(response, types.Domain)

    def create_domain(self, account: int, input: types.CreateDomainInput):
        """
        Creates a domain and the corresponding zone into the account.

        When creating a domain using Solo or Teams subscription, the DNS services
        for the zone will be automatically enabled and this will be charged on your
        following subscription renewal invoices.

        See https://developer.dnsimple.com/v2/domains/#createDomain

        :param account:
            The account id
        """
        response = self.client.post(f"/{account}/domains")
        return Response(response, types.Domain)

    def get_domain(self, account: int, domain: str):
        """
        Retrieves the details of an existing domain.

        See https://developer.dnsimple.com/v2/domains/#getDomain

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.get(f"/{account}/domains/{domain}")
        return Response(response, types.Domain)

    def delete_domain(self, account: int, domain: str):
        """
        Permanently deletes a domain from the account.

        See https://developer.dnsimple.com/v2/domains/#deleteDomain

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.delete(f"/{account}/domains/{domain}")
        return Response(
            response,
        )

    def list_collaborators(self, account: int, domain: str):
        """
        Lists collaborators for the domain.

        See https://developer.dnsimple.com/v2/domains/collaborators/#listDomainCollaborators

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.get(f"/{account}/domains/{domain}/collaborators")
        return Response(response, types.Collaborator)

    def add_collaborator(
        self, account: int, domain: str, input: types.AddCollaboratorInput
    ):
        """
        Adds a collaborator to the domain.

        At the time of the add, a collaborator may or may not have a DNSimple account. In case the collaborator doesn't have a DNSimple account, the system will invite them to register to DNSimple first and then to accept the collaboration invitation. In the other case, they are automatically added to the domain as collaborator. They can decide to reject the invitation later.

        See https://developer.dnsimple.com/v2/domains/collaborators/#addDomainCollaborator

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.post(f"/{account}/domains/{domain}/collaborators")
        return Response(response, types.Collaborator)

    def remove_collaborator(self, account: int, domain: str, collaborator: int):
        """
        Removes a collaborator from the domain.

        See https://developer.dnsimple.com/v2/domains/collaborators/#removeDomainCollaborator

        :param account:
            The account id
        :param domain:
            The domain name or id
        :param collaborator:
            The collaborator id
        """
        response = self.client.delete(
            f"/{account}/domains/{domain}/collaborators/{collaborator}"
        )
        return Response(
            response,
        )

    def get_dnssec(self, account: int, domain: str):
        """
        Gets the DNSSEC status for an existing domain.

        See https://developer.dnsimple.com/v2/domains/dnssec/#getDomainDnssec

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.get(f"/{account}/domains/{domain}/dnssec")
        return Response(response, types.DNSSEC)

    def enable_dnssec(self, account: int, domain: str):
        """
        Enables DNSSEC for the domain.

        It will enable signing of the zone. If the domain is registered with DNSimple, it will also add the DS record to the corresponding registry.

        See https://developer.dnsimple.com/v2/domains/dnssec/#enableDomainDnssec

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.post(f"/{account}/domains/{domain}/dnssec")
        return Response(response, types.DNSSEC)

    def disable_dnssec(self, account: int, domain: str):
        """
        Disables DNSSEC for the domain.

        It will disable signing of the zone. If the domain is registered with DNSimple, it will also remove the DS record at the registry corresponding to the disabled DNSSEC signing.

        See https://developer.dnsimple.com/v2/domains/dnssec/#disableDomainDnssec

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.delete(f"/{account}/domains/{domain}/dnssec")
        return Response(
            response,
        )

    def list_delegation_signer_records(self, account: int, domain: str, *, sort=None):
        """
        Lists the DS records for the domain.

        See https://developer.dnsimple.com/v2/domains/dnssec/#listDomainDelegationSignerRecords

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.get(f"/{account}/domains/{domain}/ds_records")
        return Response(response, types.DelegationSigner)

    def create_delegation_signer_record(
        self, account: int, domain: str, input: types.CreateDelegationSignerRecordInput
    ):
        """
        Adds a DS record to the domain.

        See https://developer.dnsimple.com/v2/domains/dnssec/#createDomainDelegationSignerRecord

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.post(f"/{account}/domains/{domain}/ds_records")
        return Response(response, types.DelegationSigner)

    def get_delegation_signer_record(self, account: int, domain: str, ds: int):
        """
        Retrieves the details of an existing DS record.

        See https://developer.dnsimple.com/v2/domains/dnssec/#getDomainDelegationSignerRecord

        :param account:
            The account id
        :param domain:
            The domain name or id
        :param ds:
            The delegation signer record id
        """
        response = self.client.get(f"/{account}/domains/{domain}/ds_records/{ds}")
        return Response(response, types.DelegationSigner)

    def delete_delegation_signer_record(self, account: int, domain: str, ds: int):
        """
        Removes a DS record from the domain.

        See https://developer.dnsimple.com/v2/domains/dnssec/#deleteDomainDelegationSignerRecord

        :param account:
            The account id
        :param domain:
            The domain name or id
        :param ds:
            The delegation signer record id
        """
        response = self.client.delete(f"/{account}/domains/{domain}/ds_records/{ds}")
        return Response(
            response,
        )

    def list_email_forwards(self, account: int, domain: str, *, sort=None):
        """
        Lists email forwards for the domain.

        See https://developer.dnsimple.com/v2/domains/email-forwards/#listEmailForwards

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.get(f"/{account}/domains/{domain}/email_forwards")
        return Response(response, types.EmailForward)

    def create_email_forward(
        self, account: int, domain: str, input: types.CreateEmailForwardInput
    ):
        """
        Creates a new email forward for the domain.

        See https://developer.dnsimple.com/v2/domains/email-forwards/#createEmailForward

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.post(f"/{account}/domains/{domain}/email_forwards")
        return Response(response, types.EmailForward)

    def get_email_forward(self, account: int, domain: str, emailforward: int):
        """
        Retrieves the details of an existing email forward.

        See https://developer.dnsimple.com/v2/domains/email-forwards/#getEmailForward

        :param account:
            The account id
        :param domain:
            The domain name or id
        :param emailforward:
            The email forward id
        """
        response = self.client.get(
            f"/{account}/domains/{domain}/email_forwards/{emailforward}"
        )
        return Response(response, types.EmailForward)

    def delete_email_forward(self, account: int, domain: str, emailforward: int):
        """
        Permanently deletes an email forward.

        See https://developer.dnsimple.com/v2/domains/email-forwards/#deleteEmailForward

        :param account:
            The account id
        :param domain:
            The domain name or id
        :param emailforward:
            The email forward id
        """
        response = self.client.delete(
            f"/{account}/domains/{domain}/email_forwards/{emailforward}"
        )
        return Response(
            response,
        )

    def initiate_push(self, account: int, domain: str, input: types.InitiatePushInput):
        """
        Initiates a pust of a domain to another DNSimple account.

        See https://developer.dnsimple.com/v2/domains/pushes/#initiateDomainPush

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.post(f"/{account}/domains/{domain}/pushes")
        return Response(response, types.Push)

    def list_pushes(self, account: int):
        """
        List pending pushes for the target account.

        See https://developer.dnsimple.com/v2/domains/pushes/#listPushes

        :param account:
            The account id
        """
        response = self.client.get(f"/{account}/pushes")
        return Response(response, types.Push)

    def accept_push(self, account: int, push: int, input: types.AcceptPushInput):
        """
        Accepts a push to the target account.

        See https://developer.dnsimple.com/v2/domains/pushes/#acceptPush

        :param account:
            The account id
        :param push:
            The push id
        """
        response = self.client.post(f"/{account}/pushes/{push}")
        return Response(
            response,
        )

    def reject_push(self, account: int, push: int):
        """
        Rejects a push to the target account.

        See https://developer.dnsimple.com/v2/domains/pushes/#rejectPush

        :param account:
            The account id
        :param push:
            The push id
        """
        response = self.client.delete(f"/{account}/pushes/{push}")
        return Response(
            response,
        )
