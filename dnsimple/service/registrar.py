import json
import warnings

from dnsimple.response import Response
from dnsimple.struct import DomainCheck, DomainPremiumPrice, DomainRegistration, DomainTransfer, DomainRenewal, \
    VanityNameServer, WhoisPrivacy, WhoisPrivacyRenewal, DomainPrice


class Registrar(object):
    """
    RegistrarService handles communication with the registrar related methods of the DNSimple API.

    See https://developer.dnsimple.com/v2/registrar/
    """

    def __init__(self, client):
        self.client = client

    def check_domain(self, account_id, domain):
        """
        Checks whether a domain is available to be registered.

        See https://developer.dnsimple.com/v2/registrar/#checkDomain

        :param account_id: int
            The account ID
        :param domain: str
            The domain name

        :return: dnsimple.Response
            The domain check result
        """
        response = self.client.get(f'/{account_id}/registrar/domains/{domain}/check')
        return Response(response, DomainCheck)

    def get_domain_premium_price(self, account_id, domain, options=None):
        """
        DEPERECATED: Get the premium price for a domain.
        Use get_domain_prices

        See https://developer.dnsimple.com/v2/registrar/#getDomainPremiumPrice

        :param account_id: int
            The account ID
        :param domain: str
            The domain name
        :param options: dnsimple.struct.DomainPremiumPriceOptions
            Optional action between "registration", "renewal", and "transfer".
            If omitted, it defaults to "registration".

        :return: dnsimple.Response
            The domain premium price requested
        """

        warnings.warn("DEPRECATION WARNING: get_domain_premium_price is deprecated, use get_domain_prices instead.")

        if options is None:
            options = {}
        response = self.client.get(f'/{account_id}/registrar/domains/{domain}/premium_price', params=options)
        return Response(response, DomainPremiumPrice)

    def get_domain_prices(self, account_id, domain):
        """
        Get prices for a domain.

        https://developer.dnsimple.com/v2/registrar/#getDomainPrices

        :param account_id: int
            The account ID
        :param domain: str
            The domain name

        :return: dnsimple.Response
            The domain prices
        """
        response = self.client.get(f'/{account_id}/registrar/domains/{domain}/prices')
        return Response(response, DomainPrice)

    def get_domain_registration(self, account_id, domain, domain_registration):
        """
        Get the details of an existing domain registration.

        https://developer.dnsimple.com/v2/registrar/#getDomainRegistration

        :param account_id: int
            The account ID
        :param domain: str
            The domain name
        :param domain_registration: int
            The domain registration ID

        :return: dnsimple.Response
            The domain registration
        """
        response = self.client.get(f'/{account_id}/registrar/domains/{domain}/registrations/{domain_registration}')
        return Response(response, DomainRegistration)

    def get_domain_renewal(self, account_id, domain, domain_renewal):
        """
        Get the details of an existing domain renewal.

        https://developer.dnsimple.com/v2/registrar/#getDomainRenewal

        :param account_id: int
            The account ID
        :param domain: str
            The domain name
        :param domain_renewal: int
            The domain renewal ID

        :return: dnsimple.Response
            The domain renewal
        """
        response = self.client.get(f'/{account_id}/registrar/domains/{domain}/renewals/{domain_renewal}')
        return Response(response, DomainRenewal)

    def register_domain(self, account_id, domain, request):
        """
        Registers a domain

        See https://developer.dnsimple.com/v2/registrar/#registerDomain

        :param account_id: int
            The account ID
        :param domain: str
            The domain name
        :param request: dnsimple.struct.DomainRegistrationRequest
            The attributes you can pass to register the domain

        :return: dnsimple.Response
            The newly registered domain
        """
        response = self.client.post(f'/{account_id}/registrar/domains/{domain}/registrations', request.to_json())
        return Response(response, DomainRegistration)

    def transfer_domain(self, account_id, domain, request):
        """
        Starts the transfer of a domain to DNSimple.

        See https://developer.dnsimple.com/v2/registrar/#transferDomain

        :param account_id: int
            The account ID
        :param domain: str
            The domain name
        :param request: dnsimple.struct.DomainTransferRequest
            The attributes you can pass to transfer the domain

        :return: dnsimple.Response
            The domain transfer
        """
        response = self.client.post(f'/{account_id}/registrar/domains/{domain}/transfers', request.to_json())
        return Response(response, DomainTransfer)

    def get_domain_transfer(self, account_id, domain, domain_transfer):
        """
        Retrieves the details of an existing domain transfer.

        See https://developer.dnsimple.com/v2/registrar/#getDomainTransfer

        :param account_id: int
            The account ID
        :param domain: str
            The domain name
        :param domain_transfer: int
            The domain transfer id

        :return: dnsimple.Response
            The details of an existing domain transfer
        """
        response = self.client.get(f'/{account_id}/registrar/domains/{domain}/transfers/{domain_transfer}')
        return Response(response, DomainTransfer)

    def cancel_domain_transfer(self, account_id, domain, domain_transfer):
        """
        Cancels an in progress domain transfer.

        See https://developer.dnsimple.com/v2/registrar/#cancelDomainTransfer

        :param account_id: int
            The account ID
        :param domain: str
            The domain name
        :param domain_transfer: int
            The domain transfer id

        :return: dnsimple.Response
            The details of the domain transfer
        """
        response = self.client.delete(f'/{account_id}/registrar/domains/{domain}/transfers/{domain_transfer}')
        return Response(response, DomainTransfer)

    def renew_domain(self, account_id, domain, request):
        """
        Renew a domain name already registered with DNSimple.

        Your account must be active for this command to complete successfully. You will be automatically charged the
        renewal fee upon successful renewal, so please be careful with this command.

        See https://developer.dnsimple.com/v2/registrar/#renewDomain

        :param account_id: int
            The account ID
        :param domain: str
            The domain name
        :param request: dnsimple.struct.DomainRenewRequest
            The renewal options

        :return: dnsimple.Request
            The domain renewal
        """
        response = self.client.post(f'/{account_id}/registrar/domains/{domain}/renewals', request.to_json())
        return Response(response, DomainRenewal)

    def transfer_domain_out(self, account_id, domain):
        """
        Prepare a domain for transferring out. This will unlock a domain and send the authorization code to the
        domain’s administrative contact.

        See https://developer.dnsimple.com/v2/registrar/#authorizeDomainTransferOut

        :param account_id: int
            The account ID
        :param domain: str
            The domain name

        :return: dnsimple.Response
            An empty response
        """
        response = self.client.post(f'/{account_id}/registrar/domains/{domain}/authorize_transfer_out')
        return Response(response)

    def get_domain_delegation(self, account_id, domain):
        """
        List name servers for the domain in the account.

        See https://developer.dnsimple.com/v2/registrar/delegation/#getDomainDelegation

        :param account_id: int
            The account ID
        :param domain: str
            The domain name

        :return: dnsimple.Response
            The list of name servers
        """
        response = self.client.get(f'/{account_id}/registrar/domains/{domain}/delegation')
        return Response(response, str)

    def change_domain_delegation(self, account_id, domain, new_delegation):
        """
        Update name servers for the domain in the account

        See https://developer.dnsimple.com/v2/registrar/delegation/#changeDomainDelegation

        :param account_id: int
            The account ID
        :param domain: str
            The domain name
        :param new_delegation: str[]
            The list of name servers

        :return: dnsimple.Response
            The list of name servers
        """
        response = self.client.put(f'/{account_id}/registrar/domains/{domain}/delegation', data=json.dumps(new_delegation))
        return Response(response, str)

    def change_domain_delegation_to_vanity(self, account_id, domain, new_delegation):
        """
        Delegate to vanity name servers

        WARNING: This method required the vanity name servers feature, that is only available for certain plans.
                 If the feature is not enabled, you will receive an HTTP 412 response code.

        See https://developer.dnsimple.com/v2/registrar/delegation/#changeDomainDelegationToVanity

        :param account_id: int
            The account ID
        :param domain: int/str
            The domain name or id
        :param new_delegation: str[]
            A list of name server names as strings.

        :return: dnsimple.Response
            The list of name servers
        """
        response = self.client.put(f'/{account_id}/registrar/domains/{domain}/delegation/vanity', data=json.dumps(new_delegation))
        return Response(response, VanityNameServer)

    def change_domain_delegation_from_vanity(self, account_id, domain):
        """
        Delegate from name servers

        WARNING: This method required the vanity name servers feature, that is only available for certain plans.
                 If the feature is not enabled, you will receive an HTTP 412 response code.

        See https://developer.dnsimple.com/v2/registrar/delegation/#changeDomainDelegationFromVanity

        :param account_id: int
            The account ID
        :param domain: int/str
            The domain name or id

        :return: dnsimple.Response
            An empty response
        """
        response = self.client.delete(f'/{account_id}/registrar/domains/{domain}/delegation/vanity')
        return Response(response)

    def enable_domain_auto_renewal(self, account_id, domain):
        """
        Enables auto renewal for the domain.

        See https://developer.dnsimple.com/v2/registrar/auto-renewal/#enableDomainAutoRenewal

        :param account_id: int
            The account ID
        :param domain: int/str
            The domain name or id

        :return: dnsimple.Response
            An empty response
        """
        response = self.client.put(f'/{account_id}/registrar/domains/{domain}/auto_renewal')
        return Response(response)

    def disable_domain_auto_renewal(self, account_id, domain):
        """
        Disables auto renewal for the domain.

        See https://developer.dnsimple.com/v2/registrar/auto-renewal/#disableDomainAutoRenewal

        :param account_id: int
            The account ID
        :param domain: int/str
            The domain name or id

        :return: dnsimple.Response
            An empty response
        """
        response = self.client.delete(f'/{account_id}/registrar/domains/{domain}/auto_renewal')
        return Response(response)

    def get_whois_privacy(self, account_id, domain):
        """
        Get the WHOIS privacy details for a domain

        See https://developer.dnsimple.com/v2/registrar/whois-privacy/#getWhoisPrivacy

        :param account_id: int
            The account ID
        :param domain: int/str
            The domain name or id

        :return: dnsimple.Response
            The whois privacy
        """
        response = self.client.get(f'/{account_id}/registrar/domains/{domain}/whois_privacy')
        return Response(response, WhoisPrivacy)

    def enable_whois_privacy(self, account_id, domain):
        """
        Enable WHOIS privacy

        Note that if the WHOIS privacy is not purchased for the domain, enabling WHOIS privacy will cause the service
        to be purchased for a period of 1 year.

        If WHOIS privacy was previously purchased and disabled, then calling this will enable the WHOIS privacy.

        See https://developer.dnsimple.com/v2/registrar/whois-privacy/#enableWhoisPrivacy

        :param account_id: int
            The account ID
        :param domain: int/str
            The domain name or id

        :return: dnsimple.Response
            The whois privacy
        """
        response = self.client.put(f'/{account_id}/registrar/domains/{domain}/whois_privacy')
        return Response(response, WhoisPrivacy)

    def disable_whois_privacy(self, account_id, domain):
        """
        Disable WHOIS privacy

        Note that if the WHOIS privacy is not purchased for the domain, this method will do nothing.

        If WHOIS privacy was previously purchased and enabled, then calling this will disable the WHOIS privacy.

        See https://developer.dnsimple.com/v2/registrar/whois-privacy/#disableWhoisPrivacy

        :param account_id: int
            The account ID
        :param domain: int/str
            The domain name or id

        :return: dnsimple.Response
            The whois privacy
        """
        response = self.client.delete(f'/{account_id}/registrar/domains/{domain}/whois_privacy')
        return Response(response, WhoisPrivacy)

    def renew_whois_privacy(self, account_id, domain):
        """
        Renew WHOIS privacy

        See https://developer.dnsimple.com/v2/registrar/whois-privacy/#renewWhoisPrivacy

        :param account_id: int
            The account ID
        :param domain: int/str
            The domain name or id

        :return: dnsimple.Response
            The whois privacy renewal
        """
        response = self.client.post(f'/{account_id}/registrar/domains/{domain}/whois_privacy')
        return Response(response, WhoisPrivacyRenewal)
