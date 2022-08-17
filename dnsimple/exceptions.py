class DNSimpleException(Exception):
    """
    Root Exception raised for errors in the client.

    :param message: str
        The raw response from the server
    :param errors: array[str]
        An array of error messages
    """

    def __init__(self, message=None, errors=None):
        self.message = message
        self.errors = errors
        super().__init__(self.message)

    def __str__(self):
        if self.errors is None:
            return self.message
        return f'{self.message}: {"".join(self.errors, ",")}'
