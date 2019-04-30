from requests_oauthlib import OAuth2Session
import os
import json

SCOREBOARD_URL = 'https://fantasysports.yahooapis.com/fantasy/v2/league/mlb.l.8017/scoreboard'


class Auth(object):

    def __init__(self, username, secret):
        refresh_url = 'https://api.login.yahoo.com/oauth2/get_token'
        self.token = None
        self.debug = True
        self.extra = {
            'client_id': username,
            'client_secret': secret
        }

        # Load in the token
        try:
            with open("data_file.json", "r") as read_file:
                self.token = json.load(read_file)
        except Exception as e:
            # To-Do Add in instantiating the access key
            print("Need to refresh token", e)
            raise

        self.client = OAuth2Session(self.extra['client_id'], token=self.token,
                                    auto_refresh_url=refresh_url,
                                    auto_refresh_kwargs=self.extra,
                                    token_updater=self.token_saver)
        r = None
        try:
            r = self.client.get(SCOREBOARD_URL)
            if (self.debug):
                print(r.status_code)
        except Exception as e:
            print("Cannot grab URL", e)
            raise()

    def get_url(self, url):
        return self.client.get(url)

    def token_saver(self, token):
        try:
            with open("data_file.json", "w") as write_file:
                json.dump(token, write_file)
                if(self.debug):
                    print("Wrote token to file")
        except Exception as e:
            if(self.debug):
                print("Cannot write token", e)
