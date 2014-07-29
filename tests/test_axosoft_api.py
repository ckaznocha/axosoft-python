"""
Tests.

Tests for the axosoftAPI
"""
import unittest
import os
from axosoft_api import Axosoft

if os.environ.get('TEST_ENV', 'local') == 'local':
    import axosoft_credentials

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
axosoft_user = os.environ.get('AXOSOFT_USER')
axosoft_password = os.environ.get('AXOSOFT_PASSWORD')


class TestClientCreation(unittest.TestCase):
    def setUp(self):
        self.client_id = client_id
        self.client_secret = client_secret

    def test_creation(self):
        self.axosoft_client = Axosoft(
            self.client_id, self.client_secret,
            'sublime-axosoft.axosoft.com'
        )
        self.assertIsInstance(self.axosoft_client, Axosoft)


class TestClientAuthentication(unittest.TestCase):
    def setUp(self):
        self.client_id = client_id
        self.client_secret = client_secret
        self.axosoft_client = Axosoft(
            self.client_id, self.client_secret,
            'sublime-axosoft.axosoft.com'
        )

    def test_password_auth(self):
        token = self.axosoft_client.authenticate_by_password(
            axosoft_user,
            axosoft_password
        )
        self.assertIsNotNone(token)
        is_authenticated = self.axosoft_client.is_authenticated()
        self.assertTrue(is_authenticated)
        second_token = self.axosoft_client.authenticate_by_password(
            axosoft_user,
            axosoft_password
        )
        self.assertIsNotNone(second_token)
        r = self.axosoft_client.get('me')
        self.assertEquals(axosoft_user, r['email'])
        logged_out = self.axosoft_client.log_out()
        self.assertTrue(logged_out)

    def test_code_auth(self):
        redirect_uri = "http://foo.bar/"
        url = self.axosoft_client.begin_authentication_by_code(
            redirect_uri
        )
        self.assertEquals(
            url,
            "https://sublime-axosoft.axosoft.com/auth?scope={0}&redirect_uri={1}&response_type={2}&client_id={3}"
            .format(
                "read+write",
                "http%3A%2F%2Ffoo.bar%2F",
                "code",
                self.client_id
            )
        )
        code = "db8f6d59-1a70-49a4-943d-52858646dfb0"
        token = self.axosoft_client.complete_authenticate_by_code(
            code,
            redirect_uri
        )

        self.assertIsNotNone(token)
        is_authenticated = self.axosoft_client.is_authenticated()
        self.assertTrue(is_authenticated)
        logged_out = self.axosoft_client.log_out()
        self.assertTrue(logged_out)


    def test_unauthenticated(self):
        is_authenticated = self.axosoft_client.is_authenticated()
        self.assertFalse(is_authenticated)

    def test_bad_auth_token(self):
        axosoft_client = Axosoft(
            self.client_id,
            self.client_secret,
            'sublime-axosoft.axosoft.com',
            '3et4ae1a-7025-45gt-84a3-a1391ts9a376'
        )
        is_authenticated = axosoft_client.is_authenticated()
        self.assertFalse(is_authenticated)

class TestClientMethods(unittest.TestCase):
    def setUp(self):
        self.client_id = client_id
        self.client_secret = client_secret
        self.axosoft_client = Axosoft(
            self.client_id, self.client_secret,
            'sublime-axosoft.axosoft.com'
        )
        self.axosoft_client.authenticate_by_password(
            axosoft_user,
            axosoft_password
        )

    def test_invalid_endpoint(self):
        self.assertRaises(LookupError, self.axosoft_client.get, 'foo')
        self.assertRaises(LookupError, self.axosoft_client.update, 'me', '3', {})

    def test_get_resourse(self):
        r = self.axosoft_client.get('me')
        self.assertEquals(axosoft_user, r['email'])

    def test_resourse_create(self):
        r = self.axosoft_client.create('releases', payload={'name': 'testRelease', 'release_type': {'id': 1}})
        self.assertEquals(int, type(r['id']))
        self.assertRaises(ValueError, self.axosoft_client.create, 'releases', {})

    def test_resourse_update(self):
        r = self.axosoft_client.create('releases', payload={'name': 'testRelease', 'release_type': {'id': 1}})
        r = self.axosoft_client.get('releases', r['id'])
        self.assertEquals(r['name'], 'testRelease')
        r = self.axosoft_client.update('releases', r['id'], payload={'name': 'testRelease', 'release_type': {'id': 1}})
        self.assertEquals(int, type(r['id']))
        self.assertRaises(ValueError, self.axosoft_client.update, 'releases', '', {})

    def test_resourse_delete(self):
        r = self.axosoft_client.create('releases', payload={'name': 'testRelease', 'release_type': {'id': 1}})
        r = self.axosoft_client.delete('releases', r['id'])
        self.assertTrue(r)
