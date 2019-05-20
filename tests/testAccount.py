import unittest
import logging
import fantasy_baseball
import Assets.keys

USERNAME = Assets.keys.client_id
SECRET = Assets.keys.client_secret

class TestAccount(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)
        self.account = fantasy_baseball.authenticate(USERNAME, SECRET)

    def test_environ(self):
        pass