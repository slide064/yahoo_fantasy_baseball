# encoding: utf-8

from .auth import Auth
import logging
import fantasy_baseball.get_url as get_url

class Account(object):

    def __init__(self,auth_obj):
        self.client = auth_obj
        self._get_json = get_url.get_url(self.getURL)

    def getJSON(self):
        return self._get_json
    
    def getURL(self, URL):
        return self.client.get_url(URL)