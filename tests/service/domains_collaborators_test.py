from dnsimple.struct.collaborator import Collaborator
from tests.helpers import DNSimpleMockResponse
from tests.helpers import DNSimpleTest
import responses
import unittest


class DomainCollaboratorsTest(DNSimpleTest):
    @responses.activate
    def test_list_domain_collaborators(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.GET,
                path="/1010/domains/1/collaborators",
                fixture_name="listCollaborators/success",
            )
        )

        collaborators = self.domains.list_collaborators(1010, 1).data

        self.assertEqual(2, len(collaborators))
        self.assertIsInstance(collaborators[1], Collaborator)

    @responses.activate
    def test_add_a_domain_collaborator_existing_user(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.POST,
                path="/1010/domains/1/collaborators",
                fixture_name="addCollaborator/success",
            )
        )
        collaborator = self.domains.add_collaborator(
            1010, 1, "existing-user@example.com"
        ).data

        self.assertEqual(100, collaborator.id)
        self.assertEqual("existing-user@example.com", collaborator.user_email)
        self.assertFalse(collaborator.invitation)
        self.assertIsInstance(collaborator, Collaborator)

    @responses.activate
    def test_add_a_domain_collaborator_invited_user(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.POST,
                path="/1010/domains/1/collaborators",
                fixture_name="addCollaborator/invite-success",
            )
        )
        collaborator = self.domains.add_collaborator(
            1010, 1, "invited-user@example.com"
        ).data

        self.assertEqual(101, collaborator.id)
        self.assertEqual("invited-user@example.com", collaborator.user_email)
        self.assertTrue(collaborator.invitation)
        self.assertIsInstance(collaborator, Collaborator)

    @responses.activate
    def test_remove_a_collaborator(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.DELETE,
                path="/1010/domains/1/collaborators/101",
                fixture_name="removeCollaborator/success",
            )
        )
        self.domains.remove_collaborator(1010, 1, 101)


if __name__ == "__main__":
    unittest.main()
