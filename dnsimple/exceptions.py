import warnings

class DNSimpleException(Exception):
    """
    Root Exception raised for errors in the client.

    :param message: str
        The raw response from the server
    :param attribute_errors: dict
        A dict of attribute error
    :param http_response: requests.Response
        HTTP response object
    """

    def __init__(self, message=None, attribute_errors=None, http_response=None):
        self.message = message
        self.attribute_errors = attribute_errors
        self.status = None
        self.reason = None
        self.response = None

        if http_response is not None:
            self.reason = http_response.reason
            self.status = http_response.status_code
            self.response = http_response

    def __str__(self):
        """Custom error messages for exception"""
        error_message = "({0})\n"\
                        "Reason: {1}\n".format(self.status, self.reason)

        if self.response is not None:
            error_message += "HTTP response body: {0}\n".format(self.response.text)

        return error_message

    @property
    def errors(self):
        """Return the attribute errors"""
        warnings.warn("DEPRECATION WARNING: errors is deprecated, use attribute_errors instead.")
        return self.attribute_errors
