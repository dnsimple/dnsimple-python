from requests.auth import AuthBase


class TokenAuthentication(AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = 'Bearer {token}'.format(token=self.token)
        return r
