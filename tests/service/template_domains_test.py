import unittest

import responses

from tests.helpers import DNSimpleMockResponse, DNSimpleTest


class TemplateDomainsTest(DNSimpleTest):
    @responses.activate
    def test_apply_template(self):
        responses.add(DNSimpleMockResponse(method=responses.POST,
                                           path='/1010/domains/example.com/templates/42',
                                           fixture_name='applyTemplate/success'))
        self.templates.apply_template(1010, 'example.com', 42)


if __name__ == '__main__':
    unittest.main()