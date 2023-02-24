from dnsimple.response import Response
from dnsimple.struct import Certificate, CertificateBundle, CertificatePurchase, CertificateRenewal, LetsencryptCertificateInput, LetsencryptCertificateRenewalInput


class Certificates(object):
    """The Certificates service handles communication with the certificate related methods of the DNSimple API"""

    def __init__(self, client):
        self.client = client

    def list_certificates(self, account_id, domain, page=None, per_page=None):
        """
        List the certificates for a domain in the account.

        See https://developer.dnsimple.com/v2/certificates/#listCertificates

        :param account_id: int
            The account ID
        :param domain: int/str
            The domain name or id
        :param page: int
            The page to return (default: 1)
        :param per_page: int
            The number of entries to return per page (default: 30, maximum: 100)

        :return: dnsimple.Response
            The list of certificates for the domain
        """
        response = self.client.get(f'/{account_id}/domains/{domain}/certificates', page=page, per_page=per_page)
        return Response(response, Certificate)

    def get_certificate(self, account_id, domain, certificate_id):
        """
        Get the details of a certificate.

        See https://developer.dnsimple.com/v2/certificates/#getCertificate

        :param account_id: int
            The account ID
        :param domain: int/str
            The domain name or id
        :param certificate_id: int
            The certificate id

        :return: dnsimple.Response
            The certificate requested
        """
        response = self.client.get(f'/{account_id}/domains/{domain}/certificates/{certificate_id}')
        return Response(response, Certificate)

    def download_certificate(self, account_id, domain, certificate_id):
        """
        Gets the PEM-encoded certificate, along with the root certificate and intermediate chain

        See https://developer.dnsimple.com/v2/certificates/#downloadCertificate

        :param account_id: int
            The account ID
        :param domain: int/str
            The domain name or id
        :param certificate_id: int
            The certificate id

        :return: dnsimple.Response
            The certificate in the domain
        """
        response = self.client.get(f'/{account_id}/domains/{domain}/certificates/{certificate_id}/download')
        return Response(response, CertificateBundle)

    def get_certificate_private_key(self, account_id, domain, certificate_id):
        """
        Get the PEM-encoded certificate private key

        See https://developer.dnsimple.com/v2/certificates/#getCertificatePrivateKey

        :param account_id: int
            The account ID
        :param domain: int/str
            The domain name or id
        :param certificate_id: int
            The certificate ID

        :return: dnsimple.Response
            The PEM-encoded certificate private key
        """
        response = self.client.get(f'/{account_id}/domains/{domain}/certificates/{certificate_id}/private_key')
        return Response(response, CertificateBundle)

    def purchase_letsencrypt_certificate(self, account_id, domain, certificate_input = LetsencryptCertificateInput()):
        """
        Purchase a Let's Encrypt certificate

        This method creates a new certificate order. The certificate ID should be used to request the issuance of the
        certificate using {#issue_letsencrypt_certificate}.

        See https://developer.dnsimple.com/v2/certificates/#purchaseLetsencryptCertificate

        :param account_id: int
            The account id
        :param domain: int/str
            The domain name or id
        :param certificate_input: dnsimple.struct.LetsencryptCertificateInput
            A set of attributes to purchase the Let's Encrypt certificate

        :return: dnsimple.Response
            The certificate purchase
        """
        response = self.client.post(f'/{account_id}/domains/{domain}/certificates/letsencrypt',
                                    data=certificate_input.to_json())
        return Response(response, CertificatePurchase)

    def issue_letsencrypt_certificate(self, account_id, domain, certificate_id):
        """
        Issue a pending Let's Encrypt certificate order.

        Note that the issuance process is async. A successful response means the issuance request has been successfully
        acknowledged and queued for processing.

        See https://developer.dnsimple.com/v2/certificates/#issueLetsencryptCertificate

        :param account_id: int
            The account id
        :param domain: int/str
            The domain name or id
        :param certificate_id: int
            The certificate id

        :return: dnsimple.Response
            The certificate issued
        """
        response = self.client.post(f'/{account_id}/domains/{domain}/certificates/letsencrypt/{certificate_id}/issue')
        return Response(response, Certificate)

    def purchase_letsencrypt_certificate_renewal(self, account_id, domain, certificate_id, certificate_renewal_input = LetsencryptCertificateRenewalInput()):
        """
        Purchase a Let's Encrypt certificate renewal.

        See https://developer.dnsimple.com/v2/certificates/#purchaseRenewalLetsencryptCertificate

        :param account_id: int
            The account id
        :param domain: int/str
            The domain name or id
        :param certificate_id: int
            The certificate id

        :return: dnsimple.Response
            The certificate renewal
        """
        response = self.client.post(f'/{account_id}/domains/{domain}/certificates/letsencrypt/{certificate_id}/renewals', data=certificate_renewal_input.to_json())
        return Response(response, CertificateRenewal)

    def issue_letsencrypt_certificate_renewal(self, account_id, domain, certificate_id, certificate_renewal_id):
        """
        Issue a pending Let's Encrypt certificate renewal order.

        Note that the issuance process is async. A successful response means the issuance request has been
        successfully acknowledged and queued for processing.

        See https://developer.dnsimple.com/v2/certificates/#issueRenewalLetsencryptCertificate

        :param account_id: int
            The account id
        :param domain: int/str
            The domain name or id
        :param certificate_id: int
            The certificate id
        :param certificate_renewal_id: int
            The certificate renewal id

        :return: dnsimple.Response
            The certificate to be renewed
        """
        response = self.client.post(f'/{account_id}/domains/{domain}/certificates/letsencrypt/{certificate_id}/renewals/{certificate_renewal_id}/issue')
        return Response(response, Certificate)
