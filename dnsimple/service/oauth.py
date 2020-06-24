from urllib.parse import urljoin

import urllib.parse

from dnsimple.response import Response
from dnsimple.struct import AccessToken


class Oauth(object):
    def __init__(self, client):
        self.client = client

    def exchange_authorization_for_token(self, code, client_id, client_secret, state, redirect_uri):
        """
        Exchange the short-lived authorization code for an access token
        you can use to authenticate your API calls.

        See https://developer.dnsimple.com/v2/oauth/

        :param code: str
            The authorization code, which can be used in the next step to retrieve a bearer token.
        :param client_id: str
            Client Id you received when the application was registered with DNSimple.
        :param client_secret: str
            Client Secret you received when the application was registered with DNSimple.
        :param state: str
            An unguessable random string. It is used to protect against cross-site request forgery
            attacks and it will be passed back to your redirect URI.
        :param redirect_uri: str
            Where to redirect the user after authorization has completed. This must be the exact
            URI registered or a subdirectory.
        :return: OAuthToken
            The OAuthToken object containing the access token to be used in subsequent calls to the API
        """
        response = self.client.post('/oauth/access_token', data={'code': code, 'client_id': client_id,
                                                                 'client_secret': client_secret, 'state': state,
                                                                 'redirect_uri': redirect_uri,
                                                                 'grant_type': 'authorization_code'})
        return Response(response, AccessToken)

    def authorize_url(self, client_id, redirect_uri=None, state=None, scope=None):
        """
        Generates the URL to authorize an user for an application via the OAuth2 flow.

        :param client_id: str
            The service ID you received from DNSimple when you registered the application.
        :param redirect_uri: str
            Only used to validate that it matches the original /oauth/authorize, not used to redirect again.
        :param state: str
            The state content originally passed to /oauth/authorize.
        :param scope: str
            The scopes to request from the user.
        :return: str
            The URL to redirect the user to authorize.
        """
        base_url = f'{self.client.base_url}/oauth/authorize?client_id={client_id}&response_type=code'
        query_params = {}

        if redirect_uri is not None:
            query_params['redirect_url'] = redirect_uri
        if state is not None:
            query_params['state'] = state
        if scope is not None:
            query_params['scope'] = scope

        if query_params:
            return f'{base_url}&{urllib.parse.urlencode(query_params)}'

        return base_url
