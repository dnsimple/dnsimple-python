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


class Certificates(object):
    def __init__(self, client):
        self.client = client

    def list_certificates(self, account: int, domain: str, *, sort=None):
        """
        Lists the certificates for a domain.

        See https://developer.dnsimple.com/v2/certificates/#listCertificates

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.get(f"/{account}/domains/{domain}/certificates")
        return Response(response, types.Certificate)

    def get_certificate(self, account: int, domain: str, certificate: int):
        """
        Retrieves the details of an existing certificate.

        See https://developer.dnsimple.com/v2/certificates/#getCertificate

        :param account:
            The account id
        :param domain:
            The domain name or id
        :param certificate:
            The certificate id
        """
        response = self.client.get(
            f"/{account}/domains/{domain}/certificates/{certificate}"
        )
        return Response(response, types.Certificate)

    def download_certificate(self, account: int, domain: str, certificate: int):
        """
        Gets the PEM-encoded certificate, along with the root certificate and intermediate chain.

        See https://developer.dnsimple.com/v2/certificates/#downloadCertificate

        :param account:
            The account id
        :param domain:
            The domain name or id
        :param certificate:
            The certificate id
        """
        response = self.client.get(
            f"/{account}/domains/{domain}/certificates/{certificate}/download"
        )
        return Response(response, types.CertificateDownload)

    def get_certificate_private_key(self, account: int, domain: str, certificate: int):
        """
        Gets the PEM-encoded certificate private key.

        See https://developer.dnsimple.com/v2/certificates/#getCertificatePrivateKey

        :param account:
            The account id
        :param domain:
            The domain name or id
        :param certificate:
            The certificate id
        """
        response = self.client.get(
            f"/{account}/domains/{domain}/certificates/{certificate}/private_key"
        )
        return Response(response, types.CertificatePrivateKey)

    def purchase_letsencrypt_certificate(
        self,
        account: int,
        domain: str,
        input: types.PurchaseLetsencryptCertificateInput,
    ):
        """
        Orders a [Let's Encrypt](https://dnsimple.com/letsencrypt) certificate with DNSimple.

        See https://developer.dnsimple.com/v2/certificates/#purchaseLetsencryptCertificate

        :param account:
            The account id
        :param domain:
            The domain name or id
        """
        response = self.client.post(
            f"/{account}/domains/{domain}/certificates/letsencrypt"
        )
        return Response(response, types.LetsencryptCertificatePurchase)

    def issue_letsencrypt_certificate(self, account: int, domain: str, purchaseId: int):
        """
        Issues a [Let's Encrypt](https://dnsimple.com/letsencrypt) certificate ordered with DNSimple.

        See https://developer.dnsimple.com/v2/certificates/#issueLetsencryptCertificate

        :param account:
            The account id
        :param domain:
            The domain name or id
        :param purchaseId:
            The certificate purchase order id received by `purchaseLetsencryptCertificate`.
        """
        response = self.client.post(
            f"/{account}/domains/{domain}/certificates/letsencrypt/{purchaseId}/issue"
        )
        return Response(response, types.Certificate)

    def purchase_letsencrypt_certificate_renewal(
        self,
        account: int,
        domain: str,
        certificate: int,
        input: types.PurchaseLetsencryptCertificateRenewalInput,
    ):
        """
        Renews a [Let's Encrypt](https://dnsimple.com/letsencrypt) certificate ordered with DNSimple.

        See https://developer.dnsimple.com/v2/certificates/#purchaseRenewalLetsencryptCertificate

        :param account:
            The account id
        :param domain:
            The domain name or id
        :param certificate:
            The certificate id
        """
        response = self.client.post(
            f"/{account}/domains/{domain}/certificates/letsencrypt/{certificate}/renewals"
        )
        return Response(response, types.LetsencryptCertificateRenewal)

    def issue_letsencrypt_certificate_renewal(
        self, account: int, domain: str, certificate: int, renewalId: int
    ):
        """
        Issues a [Let's Encrypt](https://dnsimple.com/letsencrypt) certificate renewal ordered with DNSimple.

        See https://developer.dnsimple.com/v2/certificates/#issueRenewalLetsencryptCertificate

        :param account:
            The account id
        :param domain:
            The domain name or id
        :param certificate:
            The certificate id
        :param renewalId:
            The certificate renewal order id received by `purchaseRenewalLetsencryptCertificate`.
        """
        response = self.client.post(
            f"/{account}/domains/{domain}/certificates/letsencrypt/{certificate}/renewals/{renewalId}/issue"
        )
        return Response(response, types.Certificate)
