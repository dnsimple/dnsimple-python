import json

from dnsimple.response import Response
from dnsimple.struct import Domain, Dnssec, Collaborator, DelegationSignerRecord, EmailForward, DomainPush


class Domains(object):
    """
    The Domains Service handles the domains endpoint of the DNSimple API.

    See https://developer.dnsimple.com/v2/domains
    """

    def __init__(self, client):
        self.client = client

    def list_domains(self, account_id, sort=None, filter=None, page=None, per_page=None):
        """
        Lists the domains in the account.

        See https://developer.dnsimple.com/v2/domains/#list

        :param account_id: int
            The account ID
        :param sort: str
            Comma separated key-value pairs: the name of a field and the order criteria (asc for ascending and desc for
            descending).

            Possible sort criteria:
                - id: Sort domains by ID (i.e. 'id:asc')
                - name: Sort domains by name (alphabetical order) (i.e. 'name:desc')
                - expiration: Sort domains by expiration date (i.e. 'expiration:asc')
        :param filter: dict
            Makes it possible to ask only for the exact subset of data that you you’re looking for.

            Possible filters:
                - name_like: Only include domains containing given string (i.e. {'name_like': 'example.com'} )
                - registrant_id: Only include domains containing given registrant ID (i.e. {'registrant_id': 1010} )
        :param page: int
            The page to return (default: 1)
        :param per_page: int
            The number of entries to return per page (default: 30, maximum: 100)

        :return: dnsimple.Response
            A list of domains
        """
        response = self.client.get(f'/{account_id}/domains', sort=sort, filter=filter, page=page, per_page=per_page)
        return Response(response, Domain)

    def create_domain(self, account_id, domain_name):
        """
        Creates a domain in the account.

        See https://developer.dnsimple.com/v2/domains/#create

        :param account_id: int
            The account ID
        :param domain_name: str
            The name of the domain
        :return: dnsimple.Response
            The newly created domain
        """
        response = self.client.post(f'/{account_id}/domains', data=json.dumps({'name': domain_name}))
        return Response(response, Domain)

    def get_domain(self, account_id, domain):
        """
        Retrieves the details of an existing domain.

        See https://developer.dnsimple.com/v2/domains/#getDomain

        :param account_id: int
            The account ID
        :param domain: int/str
            The domain name or ID
        :return: dnsimple.Response
            The domain requested
        """
        response = self.client.get(f'/{account_id}/domains/{domain}')
        return Response(response, Domain)

    def delete_domain(self, account_id, domain):
        """
        Permanently deletes a domain from the account.

        For domains which are registered with DNSimple, this will not delete the domain from the registry,
        nor perform a refund.

        See https://developer.dnsimple.com/v2/domains/#deleteDomain

        :param account_id: int
            The account ID
        :param domain: int/str
            The domain name or ID
        :return: dnsimple.Response
            An empty response
        """
        response = self.client.delete(f'/{account_id}/domains/{domain}')
        return Response(response)

    def list_collaborators(self, account_id, domain):
        """
        List collaborators for the domain in the account.

        See https://developer.dnsimple.com/v2/domains/collaborators/#listDomainCollaborators

        :param account_id: int
            The account ID
        :param domain: int/str
            The domain name or id
        :return: dnsimple.Response
            A list of collaborators for the domain in the account
        """
        response = self.client.get(f'/{account_id}/domains/{domain}/collaborators')
        return Response(response, Collaborator)

    def add_collaborator(self, account_id, domain, email):
        """
        Adds a collaborator for the domain in the account

        At the time of the add, a collaborator may or may not have a DNSimple account.

        In case the collaborator doesn't have a DNSimple account, the system will invite her/him to register to
        DNSimple first and then to accept the collaboration invitation.

        In the other case, she/he is automatically added to the domain as collaborator. She/he can decide to reject
        the invitation later.

        See https://developer.dnsimple.com/v2/domains/collaborators/#addDomainCollaborator

        :param account_id: int
            The account ID
        :param domain: int/str
            The domain name or id
        :param email: str
            The email of the collaborator to be added

        :return: dnsimple.Response
            The collaborator added to the domain in the account
        """
        response = self.client.post(f'/{account_id}/domains/{domain}/collaborators', data=json.dumps({'email': email}))
        return Response(response, Collaborator)

    def remove_collaborator(self, account_id, domain, collaborator):
        """
        Remove a collaborator from the domain in the account

        See https://developer.dnsimple.com/v2/domains/collaborators/#removeDomainCollaborator

        :param account_id: int
            The account ID
        :param domain: int/str
            The domain name or id
        :param collaborator: int
            The collaborator id

        :return: dnsimple.Response
            An empty response
        """
        response = self.client.delete(f'/{account_id}/domains/{domain}/collaborators/{collaborator}')
        return Response(response)

    def enable_dnssec(self, account_id, domain):
        """
        Enable DNSSEC for the domain in the account. This will sign the zone. If the domain is registered it will also
        add the DS record to the corresponding registry.

        See https://developer.dnsimple.com/v2/domains/dnssec/#enableDomainDnssec

        :param account_id: int
            The account ID
        :param domain: int/str
            The domain name or id

        :return: dnsimple.Response
            The DNSSEC status
        """
        response = self.client.post(f'/{account_id}/domains/{domain}/dnssec')
        return Response(response, Dnssec)

    def disable_dnssec(self, account_id, domain):
        """
        Disable DNSSEC for the domain in the account.

        See https://developer.dnsimple.com/v2/domains/dnssec/#disableDomainDnssec

        :param account_id: int
            The account ID
        :param domain: int/str
            The domain name or id

        :return: dnsimple.Response
            An empty response
        """
        response = self.client.delete(f'/{account_id}/domains/{domain}/dnssec')
        return Response(response)

    def get_dnssec(self, account_id, domain):
        """
        Get the status of DNSSEC, indicating whether it is currently enabled or disabled.

        See https://developer.dnsimple.com/v2/domains/dnssec/#getDomainDnssec

        :param account_id: int
            The account ID
        :param domain: int/str
            The domain name or id

        :return: dnsimple.Response
            The DNSSEC status requested
        """
        response = self.client.get(f'/{account_id}/domains/{domain}/dnssec')
        return Response(response, Dnssec)

    def list_domain_delegation_signer_records(self, account_id, domain, sort=None, page=None, per_page=None):
        """
        List delegation signer records for the domain in the account.

        See https://developer.dnsimple.com/v2/domains/dnssec/#listDomainDelegationSignerRecords

        :param account_id: int
            The account ID
        :param domain: int/str
            The domain name or id

        :param sort: str
            Comma separated key-value pairs: the name of a field and the order criteria (asc for ascending and desc for
            descending).

            Possible sort criteria:
                - id: Sort delegation signer records by ID (i.e. 'id:asc')
                - created_at: Sort delegation signer records by creation date (i.e. 'created_at:asc')

        :param page: int
            The page to return (default: 1)
        :param per_page: int
            The number of entries to return per page (default: 30, maximum: 100)

        :return: dnsimple.Response
            A list of delegation signer records for the domain in the account
        """
        response = self.client.get(f'/{account_id}/domains/{domain}/ds_records', sort=sort, page=page, per_page=per_page)
        return Response(response, DelegationSignerRecord)

    def create_domain_delegation_signer_record(self, account_id, domain, ds_input):
        """
        Create a delegation signer record

        You only need to create a delegation signer record manually if your domain is registered with DNSimple but
        hosted with another DNS provider that is signing your zone. To enable DNSSEC on a domain that is hosted with
        DNSimple, use the DNSSEC enable endpoint.

        See https://developer.dnsimple.com/v2/domains/dnssec/#createDomainDelegationSignerRecord

        :param account_id: int
            The account ID
        :param domain: int/str
            The domain name or id
        :param ds_input: DelegationsSignerRecordInput
            The delegation signer record input to create the delegation signer record

        :return: dnsimple.Response
            The newly created domain delegation signer record
        """
        response = self.client.post(f'/{account_id}/domains/{domain}/ds_records', data=ds_input.to_json())
        return Response(response, DelegationSignerRecord)

    def get_delegation_signer_record(self, account_id, domain, ds_record_id):
        """
        Get the delegation signer record under the domain in the account

        See https://developer.dnsimple.com/v2/domains/dnssec/#getDomainDelegationSignerRecord

        :param account_id: int
            The account ID
        :param domain: int/str
            The domain name or id
        :param ds_record_id: int
            The delegation signer record id

        :return: dnsimple.Response
            The domain delegation signer record requested
        """
        response = self.client.get(f'/{account_id}/domains/{domain}/ds_records/{ds_record_id}')
        return Response(response, DelegationSignerRecord)

    def delete_domain_delegation_signer_record(self, account_id, domain, ds_record_id):
        """
        Delete the delegation signer record under the domain in the account

        See https://developer.dnsimple.com/v2/domains/dnssec/#deleteDomainDelegationSignerRecord

        :param account_id: int
            The account ID
        :param domain: int/str
            The domain name or id
        :param ds_record_id: int
            The delegation signer record id

        :return: dnsimple.Response
            An empty response
        """
        response = self.client.delete(f'/{account_id}/domains/{domain}/ds_records/{ds_record_id}')
        return Response(response)

    def list_email_forwards(self, account_id, domain, sort=None, page=None, per_page=None):
        """
        List email forwards for the domain in the account.

        See https://developer.dnsimple.com/v2/domains/email-forwards/#listEmailForwards

        :param account_id: int
            The account ID
        :param domain: int/str
            The domain name or id
        :param sort: str
            Comma separated key-value pairs: the name of a field and the order criteria (asc for ascending and desc for
            descending).

            Possible sort criteria:
                - id: Sort email forwards by ID (i.e. 'id:asc')
                - from: Sort email forwards by from_email (aka from in alphabetical order) (i.e. 'from:desc')
                - to: Sort email forwards by to_email (aka to in alphabetical order) (i.e. 'to:asc')

        :param page: int
            The page to return (default: 1)
        :param per_page: int
            The number of entries to return per page (default: 30, maximum: 100)

        :return: dnsimple.Response
            The list of email forwards for the domain in the account
        """
        response = self.client.get(f'/{account_id}/domains/{domain}/email_forwards', sort=sort, page=page, per_page=per_page)
        return Response(response, EmailForward)

    def create_email_forward(self, account_id, domain, email_forwards_input):
        """
        Create an email forward under the domain in the account

        See https://developer.dnsimple.com/v2/domains/email-forwards/#createEmailForward

        :param account_id: int
            The account Id
        :param domain: int/str
            The domain name or id
        :param email_forwards_input:
            The email forwards input

        :return: dnsimple.Response
            The newly created email forward under the domain in the account
        """
        response = self.client.post(f'/{account_id}/domains/{domain}/email_forwards', data=json.dumps({'from': email_forwards_input.email_from, 'to': email_forwards_input.email_to}))
        return Response(response, EmailForward)

    def get_email_forward(self, account_id, domain, email_forward_id):
        """
        Get the email forward in the domain in the account

        See https://developer.dnsimple.com/v2/domains/email-forwards/#getEmailForward

        :param account_id: int
            The account ID
        :param domain: int/str
            The domain name or id
        :param email_forward_id: int
            The email forward id

        :return: dnsimple.Response
            The email forward requested
        """
        response = self.client.get(f'/{account_id}/domains/{domain}/email_forwards/{email_forward_id}')
        return Response(response, EmailForward)

    def delete_email_forward(self, account_id, domain, email_forward_id):
        """
        Delete the email forward from the domain.

        See https://developer.dnsimple.com/v2/domains/email-forwards/#deleteEmailForward

        :param account_id: int
            The account ID
        :param domain: int/str
            The domain name or id
        :param email_forward_id: int
            The email forward id

        :return: dnsimple.Response
            An empty response
        """
        response = self.client.delete(f'/{account_id}/domains/{domain}/email_forwards/{email_forward_id}')
        return Response(response)

    def initiate_push(self, account_id, domain, push_input):
        """
        Initiate a push for the domain.

        See https://developer.dnsimple.com/v2/domains/pushes/#initiate

        :param account_id: int
            The account ID
        :param domain: int/str
            The domain name or id
        :param push_input: dnsimple.struct.domain_push.DomainPushInput
            The data to send to initiate the push

        :return: dnsimple.Response
            The newly created domain push
        """
        response = self.client.post(f'/{account_id}/domains/{domain}/pushes', data=push_input.to_json())
        return Response(response, DomainPush)

    def list_pushes(self, account_id, page=None, per_page=None):
        """
       List pending pushes for the target account..

        See https://developer.dnsimple.com/v2/domains/pushes/#listPushes

        :param account_id: int
            The account ID
        :param page: int
            The page to return (default: 1)
        :param per_page: int
            The number of entries to return per page (default: 30, maximum: 100)

        :return: dnsimple.Response
            The list of pushes for the domain
        """
        response = self.client.get(f'/{account_id}/pushes', page=page, per_page=per_page)
        return Response(response, DomainPush)

    def accept_push(self, account_id, push_id, push_input):
        """
        Accept a push for the target account

        See https://developer.dnsimple.com/v2/domains/pushes/#acceptPush

        :param account_id: int
            The account ID
        :param push_id: int
            The push ID
        :param push_input: dnsimple.struct.domain_push.DomainPushInput
            The data to send to accept the push

        :return: dnsimple.Response
            An empty response
        """
        response = self.client.post(f'/{account_id}/pushes/{push_id}', data=push_input.to_json())
        return Response(response)

    def reject_push(self, account_id, push_id):
        """
        Reject a push for the target account

        See: https://developer.dnsimple.com/v2/domains/pushes/#rejectPush

        :param account_id: int
            The account ID
        :param push_id: int
            Then push ID

        :return: dnsimple.Response
            An empty response
        """
        response = self.client.delete(f'/{account_id}/pushes/{push_id}')
        return Response(response)
