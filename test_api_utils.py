import unittest
import config
from api_utils import get_auth_token, get_all_symptoms


class TestFileName(unittest.TestCase):
    def setUp(self):
        self.username = config.USERNAME
        self.password = config.PASSWORD
        self.auth_url = config.priaid_authservice_url
        self.health_url = config.priaid_healthservice_url

    def test_get_auth_token(self):
        self.assertEqual(
            type(get_auth_token(self.username, self.password, self.auth_url)),
            type('string'))

    def test_get_all_symptoms(self):
        self.assertEqual(
            type(get_all_symptoms(self.health_url,
                                  get_auth_token(self.username, self.password,
                                                 self.auth_url),
                                  config.language)),
            type([]))


if __name__ == '__main__':
    unittest.main()
