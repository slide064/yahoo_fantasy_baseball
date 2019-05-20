import os
import json
import logging
import webbrowser
from requests_oauthlib import OAuth2Session

TEST_URL = 'https://fantasysports.yahooapis.com/fantasy/v2/users;use_login=1/games'
REFRESH_URL = 'https://api.login.yahoo.com/oauth2/get_token'
TOKEN_URL = "https://api.login.yahoo.com/oauth2/request_auth"
REDIRECT_URI = "oob"
RESPONSE_TYPE = "code"
TOKEN_FILE_NAME = 'token_file.json'


class Auth(object):

    def __init__(self, username, secret):
        self.token = None
        self.debug = True
        self.extra = {
            'client_id': username,
            'client_secret': secret
        }

        # Load in the token
        try:
            with open(TOKEN_FILE_NAME, "r") as read_file:
                self.token = json.load(read_file)
                logging.debug("Successfully read token")
        except Exception as e:
            try:
                self._get_token(username, secret)
            except Exception as e:
                print("Cannot get token")
                raise

        self.client = OAuth2Session(self.extra['client_id'], token=self.token,
                                    auto_refresh_url=REFRESH_URL,
                                    auto_refresh_kwargs=self.extra,
                                    token_updater=self._token_saver)

        try:
            r = self.client.get(TEST_URL)
            logging.debug(r.status_code)
        except Exception as e:
            print("Cannot grab URL", e)
            raise

    def _get_token(self, username, secret):
        webbrowser.open("{}?client_id={}&redirect_uri={}&response_type={}".format(TOKEN_URL, username, REDIRECT_URI, RESPONSE_TYPE))
        token_input = input("Please enter the code given..")
        token = OAuth2Session(username, redirect_uri = 'oob').fetch_token(REFRESH_URL, code = token_input, client_secret = secret)
        self._token_saver(token)
        return token

    def get_url(self, url):
        return self.client.get(url)

    def _token_saver(self, token):
        try:
            with open(TOKEN_FILE_NAME, "w") as write_file:
                json.dump(token, write_file)
                logging.debug("Wrote token to file")
        except Exception as e:
            logging.debug("Could not write token to file!")
            raise