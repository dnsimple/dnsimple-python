import unittest

import responses

from dnsimple import DNSimpleException
from dnsimple.struct import DomainPremiumPriceOptions, DomainTransferRequest, DomainRenewRequest, DomainRestoreRequest
from dnsimple.struct.domain_registration import DomainRegistrationRequest
from tests.helpers import DNSimpleMockResponse, DNSimpleTest


class RegistrarTest(DNSimpleTest):
    @responses.activate
    def test_check_domain(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/registrar/domains/ruby.codes/check',
                                           fixture_name='checkDomain/success'))
        domain_check = self.registrar.check_domain(1010, 'ruby.codes').data

        self.assertEqual('ruby.codes', domain_check.domain)
        self.assertTrue(domain_check.available)
        self.assertTrue(domain_check.premium)

    @responses.activate
    def test_check_domain_premium_price(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/registrar/domains/ruby.codes/premium_price',
                                           fixture_name='getDomainPremiumPrice/success'))
        domain_premium_price = self.registrar.get_domain_premium_price(1010, 'ruby.codes').data

        self.assertEqual('109.00', domain_premium_price.premium_price)
        self.assertEqual('registration', domain_premium_price.action)

    @responses.activate
    def test_get_domain_prices(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/registrar/domains/bingo.pizza/prices',
                                           fixture_name='getDomainPrices/success'))
        domain_prices = self.registrar.get_domain_prices(1010, 'bingo.pizza').data

        self.assertEqual('bingo.pizza', domain_prices.domain)
        self.assertEqual(True, domain_prices.premium)
        self.assertEqual(20.0, domain_prices.registration_price)
        self.assertEqual(20.0, domain_prices.renewal_price)
        self.assertEqual(20.0, domain_prices.transfer_price)

    @responses.activate
    def test_get_domain_prices_for_unsupported_tld(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/registrar/domains/bingo.pizza/prices',
                                           fixture_name='getDomainPrices/failure'))
        try:
            self.registrar.get_domain_prices(1010, 'bingo.pizza')
        except DNSimpleException as dnse:
            self.assertEqual('TLD .PINEAPPLE is not supported', dnse.message)

    @responses.activate
    def test_get_domain_registration(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/registrar/domains/bingo.pizza/registrations/361',
                                           fixture_name='getDomainRegistration/success'))
        domain_registration = self.registrar.get_domain_registration(1010, 'bingo.pizza', 361).data

        self.assertEqual(domain_registration.id, 361)
        self.assertEqual(domain_registration.domain_id, 104040)
        self.assertEqual(domain_registration.registrant_id, 2715)
        self.assertEqual(domain_registration.period, 1)
        self.assertEqual(domain_registration.state, "registering")
        self.assertEqual(domain_registration.auto_renew, False)
        self.assertEqual(domain_registration.whois_privacy, False)
        self.assertEqual(domain_registration.created_at, "2023-01-27T17:44:32Z")
        self.assertEqual(domain_registration.updated_at, "2023-01-27T17:44:40Z")

    @responses.activate
    def test_get_domain_renewal(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/registrar/domains/bingo.pizza/renewals/1',
                                           fixture_name='getDomainRenewal/success'))
        domain_renewal = self.registrar.get_domain_renewal(1010, 'bingo.pizza', 1).data

        self.assertEqual(domain_renewal.id, 1)
        self.assertEqual(domain_renewal.domain_id, 999)
        self.assertEqual(domain_renewal.period, 1)
        self.assertEqual(domain_renewal.state, "renewed")
        self.assertEqual(domain_renewal.created_at, "2016-12-09T19:46:45Z")
        self.assertEqual(domain_renewal.updated_at, "2016-12-12T19:46:45Z")

    @responses.activate
    def test_check_domain_premium_price_passing_action(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/registrar/domains/ruby.codes/premium_price?action=registration',
                                           fixture_name='getDomainPremiumPrice/success'))
        self.registrar.get_domain_premium_price(1010, 'ruby.codes', DomainPremiumPriceOptions(action='registration'))

    @responses.activate
    def test_check_domain_premium_price(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/registrar/domains/example.com/premium_price',
                                           fixture_name='getDomainPremiumPrice/failure'))
        try:
            self.registrar.get_domain_premium_price(1010, 'example.com')
        except DNSimpleException as dnse:
            self.assertEqual('`example.com` is not a premium domain for registration', dnse.message)

    @responses.activate
    def test_register_domain(self):
        responses.add(DNSimpleMockResponse(method=responses.POST,
                                           path='/1010/registrar/domains/ruby.codes/registrations',
                                           fixture_name='registerDomain/success'))
        domain_registration = self.registrar.register_domain(1010, 'ruby.codes', DomainRegistrationRequest(2)).data

        self.assertEqual(1, domain_registration.id)
        self.assertEqual(999, domain_registration.domain_id)
        self.assertEqual(2, domain_registration.registrant_id)
        self.assertEqual(1, domain_registration.period)
        self.assertEqual('new', domain_registration.state)
        self.assertFalse(domain_registration.auto_renew)
        self.assertFalse(domain_registration.whois_privacy)
        self.assertEqual('2016-12-09T19:35:31Z', domain_registration.created_at)
        self.assertEqual('2016-12-09T19:35:31Z', domain_registration.updated_at)

    @responses.activate
    def test_transfer_domain(self):
        responses.add(DNSimpleMockResponse(method=responses.POST,
                                           path='/1010/registrar/domains/ruby.codes/transfers',
                                           fixture_name='transferDomain/success'))
        domain_transfer = self.registrar.transfer_domain(1010, 'ruby.codes',
                                                         DomainTransferRequest(2, 'TheAuthCode')).data

        self.assertEqual(1, domain_transfer.id)
        self.assertEqual(999, domain_transfer.domain_id)
        self.assertEqual(2, domain_transfer.registrant_id)
        self.assertEqual('transferring', domain_transfer.state)
        self.assertFalse(domain_transfer.auto_renew)
        self.assertFalse(domain_transfer.whois_privacy)
        self.assertEqual('2016-12-09T19:43:41Z', domain_transfer.created_at)
        self.assertEqual('2016-12-09T19:43:43Z', domain_transfer.updated_at)

    @responses.activate
    def test_transfer_domain_missing_auth_code(self):
        responses.add(DNSimpleMockResponse(method=responses.POST,
                                           path='/1010/registrar/domains/ruby.codes/transfers',
                                           fixture_name='transferDomain/error-missing-authcode'))
        try:
            self.registrar.transfer_domain(1010, 'ruby.codes', DomainTransferRequest(2, 'TheAuthCode'))
        except DNSimpleException as dnse:
            self.assertEqual('Validation failed', dnse.message)
            self.assertEqual('You must provide an authorization code for the domain', dnse.attribute_errors['base'][0])

    @responses.activate
    def test_transfer_domain_error(self):
        responses.add(DNSimpleMockResponse(method=responses.POST,
                                           path='/1010/registrar/domains/google.com/transfers',
                                           fixture_name='transferDomain/error-indnsimple'))
        try:
            self.registrar.transfer_domain(1010, 'google.com', DomainTransferRequest(2, 'TheAuthCode'))
        except DNSimpleException as dnse:
            self.assertEqual('The domain google.com is already in DNSimple and cannot be added', dnse.message)

    @responses.activate
    def test_get_domain_transfer(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/registrar/domains/ruby.codes/transfers/358',
                                           fixture_name='getDomainTransfer/success'))
        domain_transfer = self.registrar.get_domain_transfer(1010, 'ruby.codes', 358).data

        self.assertEqual('cancelled', domain_transfer.state)

    @responses.activate
    def test_cancel_domain_transfer(self):
        responses.add(DNSimpleMockResponse(method=responses.DELETE,
                                           path='/1010/registrar/domains/ruby.codes/transfers/358',
                                           fixture_name='cancelDomainTransfer/success'))
        domain_transfer = self.registrar.cancel_domain_transfer(1010, 'ruby.codes', 358).data

        self.assertEqual('transferring', domain_transfer.state)

    @responses.activate
    def test_renew_domain(self):
        responses.add(DNSimpleMockResponse(method=responses.POST,
                                           path='/1010/registrar/domains/ruby.codes/renewals',
                                           fixture_name='renewDomain/success'))
        domain_renewal = self.registrar.renew_domain(1010, 'ruby.codes', DomainRenewRequest(period=1)).data

        self.assertEqual(1, domain_renewal.id)
        self.assertEqual(999, domain_renewal.domain_id)
        self.assertEqual(1, domain_renewal.period)
        self.assertEqual('new', domain_renewal.state)
        self.assertEqual('2016-12-09T19:46:45Z', domain_renewal.created_at)
        self.assertEqual('2016-12-09T19:46:45Z', domain_renewal.updated_at)

    @responses.activate
    def test_renew_domain_too_early(self):
        responses.add(DNSimpleMockResponse(method=responses.POST,
                                           path='/1010/registrar/domains/example.com/renewals',
                                           fixture_name='renewDomain/error-tooearly'))
        try:
            self.registrar.renew_domain(1010, 'example.com', DomainRenewRequest(period=1))
        except DNSimpleException as dnse:
            self.assertEqual('example.com may not be renewed at this time', dnse.message)

    @responses.activate
    def test_transfer_domain_out(self):
        responses.add(DNSimpleMockResponse(method=responses.POST,
                                           path='/1010/registrar/domains/example.com/authorize_transfer_out',
                                           fixture_name='authorizeDomainTransferOut/success'))
        self.registrar.transfer_domain_out(1010, 'example.com')

    @responses.activate
    def test_restore_domain(self):
        responses.add(DNSimpleMockResponse(method=responses.POST,
                                           path='/1010/registrar/domains/ruby.codes/restores',
                                           fixture_name='restoreDomain/success'))
        domain_restore = self.registrar.restore_domain(1010, 'ruby.codes', DomainRestoreRequest()).data

        self.assertEqual(43, domain_restore.id)
        self.assertEqual(214, domain_restore.domain_id)
        self.assertEqual('new', domain_restore.state)
        self.assertEqual('2024-02-14T14:40:42Z', domain_restore.created_at)
        self.assertEqual('2024-02-14T14:40:42Z', domain_restore.updated_at)

    @responses.activate
    def test_get_domain_restore(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/registrar/domains/bingo.pizza/restores/1',
                                           fixture_name='getDomainRestore/success'))
        domain_restore = self.registrar.get_domain_restore(1010, 'bingo.pizza', 1).data

        self.assertEqual(domain_restore.id, 43)
        self.assertEqual(domain_restore.domain_id, 214)
        self.assertEqual(domain_restore.state, "new")
        self.assertEqual(domain_restore.created_at, "2024-02-14T14:40:42Z")
        self.assertEqual(domain_restore.updated_at, "2024-02-14T14:40:42Z")

if __name__ == '__main__':
    unittest.main()
