import unittest
import logging
import os
import pickle
import requests_mock
import fantasy_baseball

CLIENT_ID = os.environ['YAHOO_USER']
CLIENT_SECRET = os.environ['YAHOO_SECRET']
MO_PATH = os.path.dirname(__file__) + "\\mock_objects\\"
TOKEN_URL = 'https://api.login.yahoo.com/oauth2/get_token'
TOKEN_FILE = 'token_response.json'
TEST_URL = 'https://fantasysports.yahooapis.com/fantasy/v2/users;use_login=1/games'
LEAGUE = '431'

class TestAccount(unittest.TestCase):
    @requests_mock.Mocker()
    def setUp(self, m):
        logging.basicConfig(level=logging.INFO)
        token_file_response = MO_PATH + TOKEN_FILE
        token_file_location = MO_PATH + "token_file.json"
        logging.debug(f'Token File{token_file_location}')

        with open(token_file_response, 'r') as token_file:
            m.post(TOKEN_URL,
                    text=token_file.read())
        m.get(TEST_URL, text = "Just a test")
        self.account = fantasy_baseball.authenticate(CLIENT_ID, CLIENT_SECRET,
                                                        token_file_name=token_file_location)

    @requests_mock.Mocker()
    def test_get_URL(self, m):
        p = pickle.load(open(f'{MO_PATH}{LEAGUE}_LEAGUE_INFO.pickle','rb'))
        m.get(TEST_URL, text = p.text)
        x = self.account.getURL(TEST_URL)
        self.assertEquals(p.content, x.content)
