import unittest

import responses

from dnsimple import DNSimpleException
from dnsimple.struct import DelegationSignerRecord, DelegationSignerRecordInput
from tests.helpers import DNSimpleTest, DNSimpleMockResponse


class DomainsDelegationSignerRecordsTest(DNSimpleTest):
    @responses.activate
    def test_list_domain_delegation_signer_records(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/domains/1/ds_records',
                                           fixture_name='listDelegationSignerRecords/success'))
        delegation_signer_records = self.domains.list_domain_delegation_signer_records(1010, 1).data

        self.assertEqual(1, len(delegation_signer_records))
        self.assertIsInstance(delegation_signer_records[0], DelegationSignerRecord)

    @responses.activate
    def test_list_domain_delegation_signer_records_supports_sorting(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/domains/1/ds_records?sort'
                                               '=created_at:asc',
                                           fixture_name='listDelegationSignerRecords/success'))
        self.domains.list_domain_delegation_signer_records(1010, 1, sort='created_at:asc')

    @responses.activate
    def test_create_domain_delegation_signer_record(self):
        responses.add(DNSimpleMockResponse(method=responses.POST,
                                           path='/1010/domains/1/ds_records',
                                           fixture_name='createDelegationSignerRecord/created'))
        delegation_signer_record_input = DelegationSignerRecordInput('13',
                                                                     '684a1f049d7d082b7f98691657da5a65764913df7f065f6f8c36edf62d66ca03',
                                                                     '2', '2371')

        delegation_signer_record = self.domains.create_domain_delegation_signer_record(1010, 1,
                                                                                       delegation_signer_record_input).data

        self.assertEqual(1010, delegation_signer_record.domain_id)
        self.assertEqual(delegation_signer_record_input.get('algorithm'), delegation_signer_record.algorithm)

    @responses.activate
    def test_create_domain_delegation_signer_record_fails_validation(self):
        responses.add(DNSimpleMockResponse(method=responses.POST,
                                           path='/1010/domains/1/ds_records',
                                           fixture_name='createDelegationSignerRecord/validation-error'))

        try:
            self.domains.create_domain_delegation_signer_record(1010, 1,
                                                                DelegationSignerRecordInput(None, None, None, None))
        except DNSimpleException as dnse:
            self.assertEqual(dnse.message, 'Validation failed')
            self.assertEqual("can't be blank", dnse.errors.get('algorithm')[0])

    @responses.activate
    def test_get_domain_delegation_signer_record(self):
        responses.add(DNSimpleMockResponse(method=responses.GET,
                                           path='/1010/domains/1/ds_records/24',
                                           fixture_name='getDelegationSignerRecord/success'))

        record = self.domains.get_delegation_signer_record(1010, 1, 24).data

        self.assertEqual(24, record.id)
        self.assertEqual(1010, record.domain_id)
        self.assertEqual('8', record.algorithm)
        self.assertEqual('C1F6E04A5A61FBF65BF9DC8294C363CF11C89E802D926BDAB79C55D27BEFA94F', record.digest)
        self.assertEqual('2', record.digest_type)
        self.assertEqual('44620', record.keytag)
        self.assertEqual('2017-03-03T13:49:58Z', record.created_at)
        self.assertEqual('2017-03-03T13:49:58Z', record.updated_at)

    @responses.activate
    def test_delete_domain_delegation_signer_record(self):
        responses.add(DNSimpleMockResponse(method=responses.DELETE,
                                           path='/1010/domains/1/ds_records/24',
                                           fixture_name='deleteDelegationSignerRecord/success'))

        self.domains.delete_domain_delegation_signer_record(1010, 1, 24)


if __name__ == '__main__':
    unittest.main()
