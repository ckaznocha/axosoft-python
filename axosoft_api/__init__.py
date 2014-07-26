"""
Axosoft API.

Hook up to axosoft
"""

import requests
import json
from .validate import validate_endpoint, \
    validate_required_params, \
    validate_response


class Axosoft(object):

    """ Axosoft."""

    def __init__(self, client_id, client_secret, domain, token=None):
        """Init."""
        self.__consumer = {
            "client_id": client_id,
            "client_secret": client_secret,
            "domain": domain
        }
        self.__token = token
        self.__api_version = '3'
        self.__api_path = 'api'
        self.__base_url = 'https://{0}/{1}'\
            .format(
                self.__consumer["domain"],
                self.__api_path
            )
        self.__content_type = 'application/x-www-form-urlencoded;charset=utf-8'

    def is_authenticated(self):
        """ Test if there is a valid token."""
        if self.__token is None:
            authenticated = False
        else:
            try:
                self.get('me')
            except ValueError:
                authenticated = False
            else:
                authenticated = True

        return authenticated

    def authenticate_by_password(self, user, password):
        """
        Authenticate.

        Get a new token if one doesn't exist.
        Otherwise return the existing token.
        """
        authenticated = self.is_authenticated()
        if authenticated:
            return self.__token
        else:
            uri = '%s/oauth2/token' % self.__base_url
            payload = {
                'grant_type': 'password',
                'client_id': self.__consumer['client_id'],
                'client_secret': self.__consumer['client_secret'],
                'username': user,
                'password': password,
                'scope': 'read write'
            }
            response = requests.post(uri, payload)
            success = validate_response(response, 200)
            if success:
                auth = response.json()
                assert auth['token_type'] == 'bearer'
                self.__token = auth['access_token']
                return self.__token

    def get(self, endpoint, resourse_id=None, payload=None):
        """ Get a resource. """
        resource = validate_endpoint(endpoint, 'GET')
        uri = '{0}/v{1}/{2}'\
            .format(
                self.__base_url,
                self.__api_version,
                resource['endpoint']
            )

        if resourse_id is not None:
            uri = '{0}/{1}'.format(uri, resourse_id)
        else:
            pass

        response = requests.get(
            uri,
            params=payload,
            headers={'Authorization': 'Bearer ' + self.__token}
        )

        validate_response(response, 200)

        response = response.json()

        return response["data"]

    def create(self, endpoint, payload):
        """ Create a resource. """
        endpoint = validate_endpoint(endpoint, 'POST')

        validate_required_params(endpoint, payload)

        uri = '{0}/v{1}/{2}'\
            .format(
                self.__base_url,
                self.__api_version,
                endpoint['endpoint']
            )
        headers = {
            'Content-type': 'application/json; charset=utf-8',
            'Authorization': 'Bearer ' + self.__token
        }
        response = requests.post(
            uri,
            data=json.dumps(payload),
            headers=headers
        )

        validate_response(response, 201)

        data = response.json()
        return data['data']

    def update(self, endpoint, resourse_id, payload):
        """ Create a resource. """
        endpoint = validate_endpoint(endpoint, 'POST')

        uri = '{0}/v{1}/{2}/{3}'\
            .format(
                self.__base_url,
                self.__api_version,
                endpoint['endpoint'],
                resourse_id
            )
        headers = {
            'Content-type': 'application/json; charset=utf-8',
            'Authorization': 'Bearer ' + self.__token
        }
        response = requests.post(
            uri,
            data=json.dumps(payload),
            headers=headers
        )

        validate_response(response, 200)

        data = response.json()
        return data['data']

    def delete(self, endpoint, resourse_id):
        """ Delete a resource. """
        endpoint = validate_endpoint(endpoint, 'DELETE')

        uri = '{0}/v{1}/{2}/{3}'\
            .format(
                self.__base_url,
                self.__api_version,
                endpoint['endpoint'],
                resourse_id
            )

        headers = {'Authorization': 'Bearer ' + self.__token}

        response = requests.delete(uri, headers=headers)

        success = validate_response(response, 200)
        return success
