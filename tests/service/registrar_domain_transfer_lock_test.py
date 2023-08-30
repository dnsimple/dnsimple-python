import unittest

import responses

from dnsimple.struct import DomainTransferLock
from tests.helpers import DNSimpleMockResponse, DNSimpleTest

class RegistrarDomainTransferLockTest(DNSimpleTest):
    @responses.activate
    def test_get_domain_transfer_lock(self):
        responses.add(DNSimpleMockResponse(
            method=responses.GET,
            path="/1010/registrar/domains/101/transfer_lock",
            fixture_name="getDomainTransferLock/success",
        ))
        lock = self.registrar.get_domain_transfer_lock(
            1010,
            "101",
        ).data
        self.assertIsInstance(lock, DomainTransferLock)
        self.assertEqual(lock, DomainTransferLock({
            "enabled": True,
        }))

    @responses.activate
    def test_enable_domain_transfer_lock(self):
        responses.add(DNSimpleMockResponse(
            method=responses.POST,
            path="/1010/registrar/domains/101/transfer_lock",
            fixture_name="enableDomainTransferLock/success",
        ))
        lock = self.registrar.enable_domain_transfer_lock(
            1010,
            "101",
        ).data
        self.assertIsInstance(lock, DomainTransferLock)
        self.assertEqual(lock, DomainTransferLock({
            "enabled": True,
        }))

    @responses.activate
    def test_disable_domain_transfer_lock(self):
        responses.add(DNSimpleMockResponse(
            method=responses.DELETE,
            path="/1010/registrar/domains/101/transfer_lock",
            fixture_name="disableDomainTransferLock/success",
        ))
        lock = self.registrar.disable_domain_transfer_lock(
            1010,
            "101",
        ).data
        self.assertIsInstance(lock, DomainTransferLock)
        self.assertEqual(lock, DomainTransferLock({
            "enabled": False,
        }))
