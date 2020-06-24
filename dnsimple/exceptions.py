class DNSimpleException(Exception):
    def __init__(self, message=None, errors=None):
        self.message = message
        self.errors = errors
