# encoding: utf-8

from .auth import Auth
from .teams import Matchups
import logging

class Account(object):

    def __init__(self,auth_obj):
        self.client = auth_obj
        self.matchups = Matchups()

    def matchup(self):
        """ 
        Returns json object of all matchups 
        """
        r = self.client.get_url('https://fantasysports.yahooapis.com/fantasy/v2/league/mlb.l.8017/scoreboard')
        self.matchups.update(r)
        print(self.matchups)
    
    def teams(self):
        """
        Returns json object of all the teams
        """
        return 0