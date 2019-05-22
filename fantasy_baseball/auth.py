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

    def __init__(self, username, secret, token_file_name = TOKEN_FILE_NAME):
        self.token = None
        self.debug = True
        self.token_file_name = token_file_name
        self.extra = {
            'client_id': username,
            'client_secret': secret
        }

        # Load in the token
        try:
            with open(self.token_file_name, "r") as read_file:
                self.token = json.load(read_file)
                logging.debug("Successfully read token")         
        except:
            logging.debug(f"Could not open {self.token_file_name}")
            try:
                self._get_token(username, secret)
            except:
                logging.error("Could not get new token")
                raise

        self.client = OAuth2Session(self.extra['client_id'], token=self.token,
                                    auto_refresh_url=REFRESH_URL,
                                    auto_refresh_kwargs=self.extra,
                                    token_updater=self._token_saver)

        logging.info(self.get_url(TEST_URL))

    def _get_token(self, username, secret):
        token_location = f"{TOKEN_URL}?client_id={username}&redirect_uri={REDIRECT_URI}&response_type={RESPONSE_TYPE}"
        try:
            webbrowser.open(token_location)
        except:
            print(f"Please open {token_location} in your browser and enter code below")
        token_input = ""
        while len(token_input) != 7:
            logging.debug(token_input)
            try:
                token_input = input("Please enter the code given..")
            except:
                print("Please enter something valid")
        try:
            logging.info("Grabbing token")
            token = OAuth2Session(username, redirect_uri = 'oob').fetch_token(REFRESH_URL, code = token_input, client_secret = secret)
            logging.info("Grabbed the token successfully")
            self._token_saver(token)
        except Exception as e:
            logging.warning("Cannot write token")
            logging.warning(e)
            raise

        return token

    def get_url(self, url):
        try:
            r = self.client.get(url)
            if r.status_code == 200:
                f = r
            else:
                logging.warning(f'Cannot grab {url}, Status Code: {r.status_code}')
                f = r.status_code
        except Exception as e:
            logging.warning(f'Cannot grab {url}')
            logging.debug(e)
            f = None
        return f

    def _token_saver(self, token):
        try:
            with open(self.token_file_name, "w") as write_file:
                json.dump(token, write_file)
                logging.info(f"Wrote token to {self.token_file_name}")
        except:
            logging.error("Could not write token to file!")
            raise