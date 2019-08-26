# encoding: utf-8

from .auth import Auth
from .leagues import Leagues
import logging
import fantasy_baseball.get_url as get_url

class Account(object):

    def __init__(self,auth_obj):
        self.client = auth_obj
        self.leagues : Leagues = None
        self._get_json = get_url.get_url(self.__getURL)

    def getLeagues(self):
        if self.leagues:
            return Leagues
        else:
            self.leagues = Leagues(self._get_json)
            return self.leagues
    
    def __getURL(self, URL):
        return self.client.get_url(URL)