from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import TokenExpiredError
import os, json


class Auth(object):

    def __init__ (self,keys):
        
        refresh_url = 'https://api.login.yahoo.com/oauth2/get_token'
        self.token = None
        self.debug = True
        self.extra = {
            'client_id': keys.client_id,
            'client_secret' : keys.client_secret
        }

        #Load in the token
        try:
            with open("data_file.json", "r") as read_file:
                self.token = json.load(read_file)
        except Exception as e:
            #To-Do Add in instantiating the access key
            print("Need to refresh token")
            raise

        self.client = OAuth2Session(self.extra['client_id'], token=self.token, auto_refresh_url=refresh_url, auto_refresh_kwargs=self.extra, token_updater=self.token_saver)

        r = None
        try:
            r = self.client.get('https://fantasysports.yahooapis.com/fantasy/v2/league/mlb.l.8017/scoreboard')
            if(self.debug): print(r.status_code)
        except Exception as e:
            print(e)
            raise()

    def get_url(self,url):
        return self.client.get(url)

    def token_saver(self,token):
        try:
            with open("data_file.json", "w") as write_file:
                json.dump(token, write_file)
                if(self.debug):
                    print("Wrote token to file")
        except Exception as e:
            if(self.debug):
                print("Cannot write token")

