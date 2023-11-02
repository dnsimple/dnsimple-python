import unittest

import responses

from dnsimple import DNSimpleException
from dnsimple.struct import Charge, ChargeItem
from tests.helpers import DNSimpleMockResponse, DNSimpleTest


class BillingTest(DNSimpleTest):
    @responses.activate
    def test_list_charges_success(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/billing/charges',
                                           fixture_name='listCharges/success'))
        charges = self.billing.list_charges(1010).data

        self.assertEqual(charges, [
            Charge({"invoiced_at": "2023-08-17T05:53:36Z","total_amount": "14.50","balance_amount": "0.00","reference": "1-2","state": "collected","items":[{"description": "Register bubble-registered.com","amount": "14.50","product_id": 1,"product_type": "domain-registration","product_reference": "bubble-registered.com"}]}),
            Charge({"invoiced_at": "2023-08-17T05:57:53Z","total_amount": "14.50","balance_amount": "0.00","reference": "2-2","state": "refunded","items":[{"description": "Register example.com","amount": "14.50","product_id": 2,"product_type": "domain-registration","product_reference": "example.com"}]}),
            Charge({"invoiced_at": "2023-10-24T07:49:05Z","total_amount": "1099999.99","balance_amount": "0.00","reference": "4-2","state": "collected","items":[{"description": "Test Line Item 1","amount": "99999.99","product_id": None,"product_type": "manual","product_reference":None},{"description": "Test Line Item 2","amount": "1000000.00","product_id": None,"product_type": "manual","product_reference":None}]}),
        ])

    @responses.activate
    def test_list_charges_fail_400_bad_filter(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/billing/charges',
                                           fixture_name='listCharges/fail-400-bad-filter'))
        try:
            self.billing.list_charges(1010)
            assert False
        except DNSimpleException as e:
            self.assertEqual(e.message, "Invalid date format must be ISO8601 (YYYY-MM-DD)")

    @responses.activate
    def test_list_charges_fail_403(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/billing/charges',
                                           fixture_name='listCharges/fail-403'))
        try:
            self.billing.list_charges(1010)
            assert False
        except DNSimpleException as e:
            self.assertEqual(e.message, "Permission Denied. Required Scope: billing:*:read")

class TestCharge(unittest.TestCase):
    def test_total_amount_parsing(self):
        charge = Charge({'total_amount': '100.50', 'balance_amount': None})
        self.assertEqual(charge.total_amount, 100.5)

    def test_balance_amount_parsing(self):
        charge = Charge({'total_amount': None, 'balance_amount': '50.25'})
        self.assertEqual(charge.balance_amount, 50.25)

    def test_none_values(self):
        charge = Charge({'total_amount': None, 'balance_amount': None})
        self.assertIsNone(charge.total_amount)
        self.assertIsNone(charge.balance_amount)

class TestChargeItem(unittest.TestCase):
    def test_amount_parsing(self):
        charge = ChargeItem({'amount': '100.50'})
        self.assertEqual(charge.amount, 100.5)

    def test_none_values(self):
        charge = ChargeItem({'amount': None})
        self.assertIsNone(charge.amount)
