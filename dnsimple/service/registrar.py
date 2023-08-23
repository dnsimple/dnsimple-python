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


class Registrar(object):
    def __init__(self, client):
        self.client = client

    def check_domain(self, account: int, domain: str):
        """
        Checks a domain name for availability.

        See https://developer.dnsimple.com/v2/registrar/#checkDomain

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.get(f"/{account}/registrar/domains/{domain}/check")
        return Response(response, types.DomainCheckResult)

    def get_domain_premium_price(self, account: int, domain: str, *, action=None):
        """
        Deprecated in favor of getDomainPrices.

        Retrieves the premium price for a premium domain.

        Please note that a premium price can be different for registration, renewal, transfer. By default this endpoint returns the premium price for registration. If you need to check a different price, you should specify it with the action param.

        See https://developer.dnsimple.com/v2/registrar/#getDomainPremiumPrice

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.get(
            f"/{account}/registrar/domains/{domain}/premium_price"
        )
        return Response(response, types.DomainPremiumPrice)

    def get_domain_prices(self, account: int, domain: str):
        """
        Retrieve domain prices.

        See https://developer.dnsimple.com/v2/registrar/#getDomainPrices

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.get(f"/{account}/registrar/domains/{domain}/prices")
        return Response(response, types.DomainPrices)

    def register_domain(
        self, account: int, domain: str, input: types.RegisterDomainInput
    ):
        """
        Registers a domain name.

        Your account must be active for this command to complete successfully. You will be automatically charged the registration fee upon successful registration, so please be careful with this command.

        When registering a domain using Solo or Teams subscription, the DNS services
        for the zone will be automatically enabled and this will be charged on your
        following subscription renewal invoices.

        See https://developer.dnsimple.com/v2/registrar/#registerDomain

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.post(
            f"/{account}/registrar/domains/{domain}/registrations"
        )
        return Response(response, types.DomainRegistration)

    def get_domain_registration(
        self, account: int, domain: str, domainregistration: int
    ):
        """
        Retrieves the details of an existing domain registration.

        See https://developer.dnsimple.com/v2/registrar/#getDomainRegistration

        :param account:
            The account id
        :param domain:
            The domain name or id
        :param domainregistration:
            The domain registration id
        """
        response = self.client.get(
            f"/{account}/registrar/domains/{domain}/registrations/{domainregistration}"
        )
        return Response(response, types.DomainRegistration)

    def transfer_domain(
        self, account: int, domain: str, input: types.TransferDomainInput
    ):
        """
        Transfers a domain name from another registrar.

        Your account must be active for this command to complete successfully. You will be automatically charged the 1-year transfer fee upon successful transfer, so please be careful with this command. The transfer may take anywhere from a few minutes up to 7 days.

        When transfering a domain using Solo or Teams subscription, the DNS services
        for the zone will be automatically enabled and this will be charged on your
        following subscription renewal invoices.

        See https://developer.dnsimple.com/v2/registrar/#transferDomain

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.post(f"/{account}/registrar/domains/{domain}/transfers")
        return Response(response, types.DomainTransfer)

    def get_domain_transfer(self, account: int, domain: str, domaintransfer: int):
        """
        Retrieves the details of an existing domain transfer.

        See https://developer.dnsimple.com/v2/registrar/#getDomainTransfer

        :param account:
            The account id
        :param domain:
            The domain name or id
        :param domaintransfer:
            The domain transfer id
        """
        response = self.client.get(
            f"/{account}/registrar/domains/{domain}/transfers/{domaintransfer}"
        )
        return Response(response, types.DomainTransfer)

    def cancel_domain_transfer(self, account: int, domain: str, domaintransfer: int):
        """
        Cancels an in progress domain transfer.

        See https://developer.dnsimple.com/v2/registrar/#cancelDomainTransfer

        :param account:
            The account id
        :param domain:
            The domain name or id
        :param domaintransfer:
            The domain transfer id
        """
        response = self.client.delete(
            f"/{account}/registrar/domains/{domain}/transfers/{domaintransfer}"
        )
        return Response(response, types.DomainTransfer)

    def renew_domain(self, account: int, domain: str, input: types.RenewDomainInput):
        """
        Explicitly renews a domain, if the registry supports this function.

        Your account must be active for this command to complete successfully. You will be automatically charged the renewal fee upon successful renewal, so please be careful with this command.

        See https://developer.dnsimple.com/v2/registrar/#domainRenew

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.post(f"/{account}/registrar/domains/{domain}/renewals")
        return Response(response, types.DomainRenewal)

    def get_domain_renewal(self, account: int, domain: str, domainrenewal: int):
        """
        Retrieves the details of an existing domain renewal.

        See https://developer.dnsimple.com/v2/registrar/#getDomainRenewal

        :param account:
            The account id
        :param domain:
            The domain name or id
        :param domainrenewal:
            The domain renewal id
        """
        response = self.client.get(
            f"/{account}/registrar/domains/{domain}/renewals/{domainrenewal}"
        )
        return Response(response, types.DomainRenewal)

    def transfer_domain_out(self, account: int, domain: str):
        """
        Prepares a domain for transferring out.

        This will unlock a domain and send the authorization code to the domain's administrative contact.

        See https://developer.dnsimple.com/v2/registrar/#authorizeDomainTransferOut

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.post(
            f"/{account}/registrar/domains/{domain}/authorize_transfer_out"
        )
        return Response(
            response,
        )

    def get_domain_delegation(self, account: int, domain: str):
        """
        Lists the name servers for the domain.

        See https://developer.dnsimple.com/v2/registrar/delegation/#getDomainDelegation

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.get(f"/{account}/registrar/domains/{domain}/delegation")
        return Response(response, types.DomainNameServer)

    def change_domain_delegation(self, account: int, domain: str, input: List[str]):
        """
        Changes the domain name servers.

        See https://developer.dnsimple.com/v2/registrar/delegation/#changeDomainDelegation

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.put(f"/{account}/registrar/domains/{domain}/delegation")
        return Response(response, types.DomainNameServer)

    def change_domain_delegation_to_vanity(
        self, account: int, domain: str, input: List[str]
    ):
        """
        Delegate a domain to vanity name servers.

        See https://developer.dnsimple.com/v2/registrar/delegation/#changeDomainDelegationToVanity

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.put(
            f"/{account}/registrar/domains/{domain}/delegation/vanity"
        )
        return Response(response, types.NameServer)

    def change_domain_delegation_from_vanity(self, account: int, domain: str):
        """
        De-delegate a domain from vanity name servers.

        See https://developer.dnsimple.com/v2/registrar/delegation/#changeDomainDelegationFromVanity

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.delete(
            f"/{account}/registrar/domains/{domain}/delegation/vanity"
        )
        return Response(
            response,
        )

    def enable_domain_auto_renewal(self, account: int, domain: str):
        """
        Enables auto renewal for the domain.

        See https://developer.dnsimple.com/v2/registrar/#enableDomainAutoRenewal

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.put(
            f"/{account}/registrar/domains/{domain}/auto_renewal"
        )
        return Response(
            response,
        )

    def disable_domain_auto_renewal(self, account: int, domain: str):
        """
        Disables auto renewal for the domain.

        See https://developer.dnsimple.com/v2/registrar/#disableDomainAutoRenewal

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.delete(
            f"/{account}/registrar/domains/{domain}/auto_renewal"
        )
        return Response(
            response,
        )

    def get_whois_privacy(self, account: int, domain: str):
        """
        Gets the whois privacy status for an existing domain.

        See https://developer.dnsimple.com/v2/registrar/whois-privacy/#getWhoisPrivacy

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.get(
            f"/{account}/registrar/domains/{domain}/whois_privacy"
        )
        return Response(response, types.WhoisPrivacy)

    def enable_whois_privacy(self, account: int, domain: str):
        """
        Enables the WHOIS privacy for the domain.

        Note that if the WHOIS privacy is not purchased for the domain, enabling WHOIS privacy will cause the service to be purchased for a period of 1 year. If WHOIS privacy was previously purchased and disabled, then calling this will enable the WHOIS privacy.

        See https://developer.dnsimple.com/v2/registrar/whois-privacy/#enableWhoisPrivacy

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.put(
            f"/{account}/registrar/domains/{domain}/whois_privacy"
        )
        return Response(response, types.WhoisPrivacy)

    def disable_whois_privacy(self, account: int, domain: str):
        """
        Disables the WHOIS privacy for the domain.

        See https://developer.dnsimple.com/v2/registrar/whois-privacy/#disableWhoisPrivacy

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.delete(
            f"/{account}/registrar/domains/{domain}/whois_privacy"
        )
        return Response(response, types.WhoisPrivacy)

    def renew_whois_privacy(self, account: int, domain: str):
        """
        Renews the WHOIS privacy for the domain.

        Note that if the WHOIS privacy was never purchased for the domain or if there is another renewal order in progress, renewing WHOIS privacy will return an error.

        See https://developer.dnsimple.com/v2/registrar/whois-privacy/#renewWhoisPrivacy

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.post(
            f"/{account}/registrar/domains/{domain}/whois_privacy/renewals"
        )
        return Response(response, types.WhoisPrivacyRenewal)

    def list_registrant_changes(
        self, account: int, *, sort=None, state=None, domain_id=None, contact_id=None
    ):
        """
        List registrant changes in the account.

        See https://developer.dnsimple.com/v2/registrar/#listRegistrantChanges

        :param account:
            The account id
        """
        response = self.client.get(f"/{account}/registrar/registrant_changes")
        return Response(response, types.RegistrantChange)

    def create_registrant_change(
        self, account: int, input: types.CreateRegistrantChangeInput
    ):
        """
        Start registrant change.

        See https://developer.dnsimple.com/v2/registrar/#createRegistrantChange

        :param account:
            The account id
        """
        response = self.client.post(f"/{account}/registrar/registrant_changes")
        return Response(response, types.RegistrantChange)

    def check_registrant_change(
        self, account: int, input: types.CheckRegistrantChangeInput
    ):
        """
        Retrieves the requirements of a registrant change.

        See https://developer.dnsimple.com/v2/registrar/#checkRegistrantChange

        :param account:
            The account id
        """
        response = self.client.post(f"/{account}/registrar/registrant_changes/check")
        return Response(response, types.RegistrantChangeCheck)

    def get_registrant_change(self, account: int, registrantchange: int):
        """
        Retrieves the details of an existing registrant change.

        See https://developer.dnsimple.com/v2/registrar/#getRegistrantChange

        :param account:
            The account id
        :param registrantchange:
            The registrant change id
        """
        response = self.client.get(
            f"/{account}/registrar/registrant_changes/{registrantchange}"
        )
        return Response(response, types.RegistrantChange)

    def delete_registrant_change(self, account: int, registrantchange: int):
        """
        Cancel an ongoing registrant change from the account.

        See https://developer.dnsimple.com/v2/registrar/#deleteRegistrantChange

        :param account:
            The account id
        :param registrantchange:
            The registrant change id
        """
        response = self.client.delete(
            f"/{account}/registrar/registrant_changes/{registrantchange}"
        )
        return Response(
            response,
        )
