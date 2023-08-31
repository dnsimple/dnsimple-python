from dataclasses import asdict
import unittest

import responses

from dnsimple.struct.registrant import (
    CheckRegistrantChangeInput,
    CreateRegistrantChangeInput,
    RegistrantChange,
    RegistrantChangeCheck,
)
from tests.helpers import DNSimpleMockResponse, DNSimpleTest


class RegistrarRegistrantTest(DNSimpleTest):
    @responses.activate
    def test_check_registrant_change(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.POST,
                path="/1010/registrar/registrant_changes/check",
                fixture_name="checkRegistrantChange/success",
            )
        )
        res = self.registrar.check_registrant_change(
            1010,
            CheckRegistrantChangeInput(
                domain_id=101,
                contact_id=101,
            ),
        ).data

        self.assertEqual(
            res,
            RegistrantChangeCheck(
                {
                    "domain_id": 101,
                    "contact_id": 101,
                    "extended_attributes": [],
                    "registry_owner_change": True,
                }
            ),
        )

    @responses.activate
    def test_create_registrant_change(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.POST,
                path="/1010/registrar/registrant_changes",
                fixture_name="createRegistrantChange/success",
            )
        )
        res = self.registrar.create_registrant_change(
            1010,
            CreateRegistrantChangeInput(
                contact_id=101,
                domain_id=101,
                extended_attributes={},
            ),
        ).data

        self.assertEqual(
            res,
            RegistrantChange(
                {
                    "id": 101,
                    "account_id": 101,
                    "domain_id": 101,
                    "contact_id": 101,
                    "state": "new",
                    "extended_attributes": {},
                    "registry_owner_change": True,
                    "irt_lock_lifted_by": None,
                    "created_at": "2017-02-03T17:43:22Z",
                    "updated_at": "2017-02-03T17:43:22Z",
                }
            ),
        )

    @responses.activate
    def test_delete_registrant_change(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.DELETE,
                path="/1010/registrar/registrant_changes/101",
                fixture_name="deleteRegistrantChange/success",
            )
        )
        res = self.registrar.delete_registrant_change(1010, 101).data

        self.assertEqual(res, None)

    @responses.activate
    def test_get_registrant_change(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.GET,
                path="/1010/registrar/registrant_changes/101",
                fixture_name="getRegistrantChange/success",
            )
        )
        res = self.registrar.get_registrant_change(1010, 101).data

        self.assertEqual(
            res,
            RegistrantChange(
                {
                    "id": 101,
                    "account_id": 101,
                    "domain_id": 101,
                    "contact_id": 101,
                    "state": "new",
                    "extended_attributes": {},
                    "registry_owner_change": True,
                    "irt_lock_lifted_by": None,
                    "created_at": "2017-02-03T17:43:22Z",
                    "updated_at": "2017-02-03T17:43:22Z",
                }
            ),
        )

    @responses.activate
    def test_list_registrant_changes(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.GET,
                path="/1010/registrar/registrant_changes",
                fixture_name="listRegistrantChanges/success",
            )
        )
        res = self.registrar.list_registrant_changes(1010).data

        self.assertEqual(
            res,
            [
                RegistrantChange(
                    {
                        "id": 101,
                        "account_id": 101,
                        "domain_id": 101,
                        "contact_id": 101,
                        "state": "new",
                        "extended_attributes": {},
                        "registry_owner_change": True,
                        "irt_lock_lifted_by": None,
                        "created_at": "2017-02-03T17:43:22Z",
                        "updated_at": "2017-02-03T17:43:22Z",
                    }
                )
            ],
        )


if __name__ == "__main__":
    unittest.main()
