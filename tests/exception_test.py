from dnsimple import DNSimpleException
from dnsimple.response import Response
from dnsimple.struct import Domain
from tests.helpers import DNSimpleMockResponse
from tests.helpers import DNSimpleTest
import responses
import unittest


class ExceptionTest(DNSimpleTest):
    @responses.activate
    def test_bad_request_exception(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.POST,
                path="/1010/domains",
                fixture_name="validation-error",
            )
        )
        try:
            self.domains.create_domain(1010, "example-beta.com")
        except DNSimpleException as ex:
            self.assertEqual(ex.status, 400)
            self.assertEqual(ex.reason, "Bad Request")
            self.assertEqual(ex.message, "Validation failed")
            self.assertEqual(
                ex.attribute_errors,
                {
                    "address1": ["can't be blank"],
                    "city": ["can't be blank"],
                    "country": ["can't be blank"],
                    "email": ["can't be blank", "is an invalid email address"],
                    "first_name": ["can't be blank"],
                    "last_name": ["can't be blank"],
                    "phone": ["can't be blank", "is probably not a phone number"],
                    "postal_code": ["can't be blank"],
                    "state_province": ["can't be blank"],
                },
            )
            self.assertEqual(
                str(ex),
                "(400)\nReason: Bad Request\nHTTP response body: {0}\n".format(
                    ex.response.text
                ),
            )

    @responses.activate
    def test_not_found_exception(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.POST,
                path="/1010/domains",
                fixture_name="notfound-domain",
            )
        )
        try:
            self.domains.create_domain(1010, "example-beta.com")
        except DNSimpleException as ex:
            self.assertEqual(ex.status, 404)
            self.assertEqual(ex.reason, "Not Found")
            self.assertEqual(ex.message, "Domain `0` not found")
            self.assertEqual(ex.attribute_errors, None)
            self.assertEqual(
                str(ex),
                '(404)\nReason: Not Found\nHTTP response body: {"message":"Domain `0` not found"}\n',
            )

    @responses.activate
    def test_no_body_exception(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.POST,
                path="/1010/domains",
                fixture_name="method-not-allowed",
            )
        )
        try:
            self.domains.create_domain(1010, "example-beta.com")
        except DNSimpleException as ex:
            self.assertEqual(ex.status, 405)
            self.assertEqual(ex.reason, "Method Not Allowed")
            self.assertEqual(ex.message, None)
            self.assertEqual(ex.attribute_errors, None)

    @responses.activate
    def test_backward_compat_errors_attr_exception(self):
        responses.add(
            DNSimpleMockResponse(
                method=responses.POST,
                path="/1010/domains",
                fixture_name="validation-error",
            )
        )
        try:
            self.domains.create_domain(1010, "example-beta.com")
        except DNSimpleException as ex:
            self.assertIsNotNone(ex.attribute_errors)
            self.assertIsNotNone(ex.errors)
            self.assertEqual(ex.errors, ex.attribute_errors)


if __name__ == "__main__":
    unittest.main()
