from dnsimple import DNSimpleException
from dnsimple.extra import attach_attributes_to, return_list_of


class Response(object):
    """
    Wrapper holding the whole http response as well as the data returned
    by an call to an endpoint of the DNSimple API.

    """

    http_response = None
    """The raw HTTP response from the DNSimple API call"""
    headers = None
    """The HTTP headers"""
    rate_limit = None
    """The maximum number of requests you can perform per hour."""
    rate_limit_remaining = None
    """The number of requests remaining in the current rate limit window."""
    rate_limit_reset = None
    """The time at which the current rate limit window in Unix time format."""
    data = None
    """The data returned from the DNSimple API call wrapped inside an object"""
    pagination = None
    """The pagination information wrapped in a Pagination object"""

    def __init__(self, http_response, obj=None):
        """

        :param http_response: requests.Response
            The raw response from the server
        :param obj: object
            An object encapsulating the data (json) in the response

        :raises DNSimpleException
            When the server responds with an error code
        """
        if int(http_response.status_code) in range(400, 504):
            if http_response.text != '':
                message = http_response.json().get('message')
                attribute_errors = http_response.json().get('errors')
                raise DNSimpleException(message=message, attribute_errors=attribute_errors, http_response=http_response)

            raise DNSimpleException(http_response=http_response)

        self.__class__.http_response = http_response
        self.__class__.headers = self.__class__.http_response.headers
        self.__class__.rate_limit = int(self.__class__.headers['X-RateLimit-Limit'])
        self.__class__.rate_limit_remaining = int(self.__class__.headers['X-RateLimit-Remaining'])
        self.__class__.rate_limit_reset = int(self.__class__.headers['X-RateLimit-Reset'])

        self.add_data(obj, http_response)

        if http_response.status_code != 204:
            self.__class__.pagination = None if http_response.json().get('pagination') is None else Pagination(
                http_response.json().get('pagination'))

    def add_data(self, obj, http_response):
        raw_json = None

        if obj is not None:
            raw_json = http_response.json()
        if obj is None:
            self.__class__.data = None
        elif 'data' not in raw_json:
            self.__class__.data = obj(raw_json)
        elif type(raw_json.get('data')) is list:
            self.__class__.data = return_list_of(obj, raw_json.get('data'))
        else:
            self.__class__.data = obj(raw_json.get('data'))


class Pagination(object):
    """
    The pagination object

    Any API endpoint that returns a list of items requires pagination. By default we will return 30 records from any
    listing endpoint.

    If an API endpoint returns a list of items, then it will include a pagination object that contains pagination
    information.

    See https://developer.dnsimple.com/v2/#pagination
    """

    current_page = None
    """The page currently returned (default: 1)"""
    per_page = None
    """The number of entries returned per page (default: 30)"""
    total_entries = None
    """The total number of entries available in the entire collection"""
    total_pages = 1
    """The total number of pages available given the current per_page value"""

    def __init__(self, data):
        attach_attributes_to(self, data)
